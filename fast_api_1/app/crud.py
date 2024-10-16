# CRUD (Create, Read, Update, Delete)

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models import ORM_CLASS, ORM_OBJECT
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select


async def add_item(session: AsyncSession, item: ORM_OBJECT) -> ORM_OBJECT:
    session.add(item)
    try:
        await session.commit()
    except IntegrityError as err:
        if err.orig.pgcode == "23505":
            raise HTTPException(status_code=409, detail="Item already exists")
        raise err
    return item


async def get_item(session: AsyncSession, orm_cls: ORM_CLASS, item_id: int) -> ORM_OBJECT:
    orm_obj = await session.get(orm_cls, item_id)

    if orm_obj is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return orm_obj


async def search_item(session: AsyncSession, orm_cls: ORM_CLASS, qs_param: str):
    statement = select(orm_cls).where(orm_cls.description.like(f"%{qs_param}%"))
    orm_obj = await session.execute(statement)
    result = orm_obj.scalars().all()

    if result is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return JSONResponse(content=jsonable_encoder(result))


async def delete_item(session: AsyncSession, orm_cls: ORM_CLASS, item_id) -> None:
    orm_obj = await get_item(session, orm_cls, item_id)
    await session.delete(orm_obj)
    await session.commit()

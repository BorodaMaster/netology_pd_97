# CRUD (Create, Read, Update, Delete)
import json

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models import ORM_CLASS, ORM_OBJECT
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text


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


async def search_item(session: AsyncSession, qs_param: str) -> ORM_OBJECT:
    orm_obj = await session.execute(text(f"SELECT * FROM advertisements WHERE advertisements.description LIKE "
                                         f"'%{qs_param}%'"))

    if orm_obj is None:
        raise HTTPException(status_code=404, detail="Item not found")

    result = orm_obj.mappings().all()

    return JSONResponse(content=jsonable_encoder(result))


async def delete_item(session: AsyncSession, orm_cls: ORM_CLASS, item_id) -> None:
    orm_obj = await get_item(session, orm_cls, item_id)
    await session.delete(orm_obj)
    await session.commit()

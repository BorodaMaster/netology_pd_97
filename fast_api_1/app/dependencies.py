from typing import Annotated

from fastapi import Depends
from models import SessionDB
from sqlalchemy.ext.asyncio import AsyncSession


async def get_session() -> AsyncSession:
    async with SessionDB() as session:
        return session


SessionDependency = Annotated[AsyncSession, Depends(get_session)]

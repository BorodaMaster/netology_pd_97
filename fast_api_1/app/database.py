from contextlib import asynccontextmanager
from fastapi import FastAPI
from models import engine, Base


@asynccontextmanager
async def connect_db(app: FastAPI):
    print("START SERVER...")
    async with engine.begin() as session:
        await session.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()
    print("STOP SERVER...")

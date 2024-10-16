import os

from sqlalchemy import String, Integer
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

POSTGRES_DB = os.getenv("POSTGRES_DB", "swapi")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "RtpZV7ow")

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "127.0.0.1")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5434")

PG_DSN = (
    f"postgresql+asyncpg://"
    f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
    f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

engine = create_async_engine(PG_DSN)
SessionDB = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase, AsyncAttrs):
    pass


class SwapiPeople(Base):
    __tablename__ = "swapi_people"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    birth_year: Mapped[str] = mapped_column(String(64), nullable=False)
    eye_color: Mapped[str] = mapped_column(String(64), nullable=False)
    films: Mapped[str] = mapped_column(String(256), nullable=False)
    gender: Mapped[str] = mapped_column(String(64), nullable=False)
    hair_color: Mapped[str] = mapped_column(String(64), nullable=False)
    height: Mapped[str] = mapped_column(String(64), nullable=False)
    homeworld: Mapped[str] = mapped_column(String(64), nullable=False)
    mass: Mapped[str] = mapped_column(String(64), nullable=False)
    name: Mapped[str] = mapped_column(String(64), nullable=False)
    skin_color: Mapped[str] = mapped_column(String(64), nullable=False)
    species: Mapped[str.join()] = mapped_column(String(256), nullable=False)
    starships: Mapped[str.join()] = mapped_column(String(256), nullable=False)
    vehicles: Mapped[str.join()] = mapped_column(String(256), nullable=False)


async def init_orm():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

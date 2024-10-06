import os
import datetime

from sqlalchemy import create_engine, Integer, String, DateTime, func
from sqlalchemy.orm import sessionmaker, mapped_column, DeclarativeBase, Mapped
from atexit import register

POSTGRES_DB = os.getenv("POSTGRES_DB", "postgres")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "RtpZV7ow")

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "127.0.0.1")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5433")

PG_DSN = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(PG_DSN)

Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class Advertisement(Base):
    __tablename__ = "advertisements"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    header: Mapped[str] = mapped_column(String(64), nullable=False)
    description: Mapped[str] = mapped_column(String(256), nullable=False)
    owner: Mapped[str] = mapped_column(String(32), nullable=False)
    date_creation: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now())

    @property
    def json(self):
        return {
            "id": self.id,
            "header": self.header,
            "description": self.description,
            "owner": self.owner,
            "date_creation": self.date_creation.isoformat()
        }


# Create table
Base.metadata.create_all(bind=engine)

# Close connection to server
register(engine.dispose)

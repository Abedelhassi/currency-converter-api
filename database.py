import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base


DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg://admin:secret@localhost:5433/currency_db")


engine = create_async_engine(DATABASE_URL, echo=True)


async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


Base = declarative_base()

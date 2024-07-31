import os

from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv('.env')

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    user_token = Column(String)
    role = Column(String)


engine = create_async_engine(os.environ['DATABASE_URL'])

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)

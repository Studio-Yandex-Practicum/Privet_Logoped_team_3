from sqlalchemy import Column, Integer, String, Bool
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    user_token = Column(String)
    is_auth = Column(Bool)
    is_admin = Column(Bool)
    role = Column(String)

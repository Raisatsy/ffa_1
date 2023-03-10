from datetime import datetime

from db.base import Base
from sqlalchemy import Column, String, Integer, DateTime, func


class User(Base):
    __tablename__ = 'user'

    created_at = Column(DateTime, index=True, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), server_onupdate=func.now(), onupdate=datetime.now)
    username = Column(String(128), index=True, nullable=False)
    first_name = Column(String(64), )
    last_name = Column(String(64), )
    age = Column(Integer, nullable=False)

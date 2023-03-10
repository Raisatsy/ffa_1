from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel
from pydantic.dataclasses import dataclass


class UserSchema(BaseModel):
    id: int
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    age: int
    created_at: datetime

    class Config:
        orm_mode = True


class UpdateUserSchema(BaseModel):
    id: Optional[int]
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    age: Optional[str]
    created_at: Optional[datetime]


class UserList(BaseModel):
    count: int
    users: List[UserSchema]

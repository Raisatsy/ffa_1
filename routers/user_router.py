from datetime import datetime

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.future import select
from starlette.responses import Response
from sqlalchemy.ext.asyncio import AsyncSession

from db.engine import get_async_session
from db import User
from routers.schemas import UserList, UserSchema, UpdateUserSchema



user_router = APIRouter(prefix='/users', tags=['Пользователи'])


@user_router.get('/', name='Все пользователи', response_model=UserList)
def get_all_users():
    return UserList(count=len(users), users=users)


@user_router.post('/', name='Добавить пользователя', response_model=UserSchema)
def create_user(user: UserSchema):
    users.append(user)
    return user


@user_router.get('/{user_id}', name='Получить пользователя', response_model=UserSchema)
async def get_user(user_id: int, session: AsyncSession = Depends(get_async_session)):
    q = select(User).where(User.id == user_id)
    user = (await session.execute(q)).scalars().first()
    if user is not None:
        return UserSchema.from_orm(user)
    raise HTTPException(status_code=404, detail='User not found')



@user_router.delete('/{user_id}', name='Удалить пользователя', response_class=Response)
def delete_user(user_id: int):
    for i, user in enumerate(tuple(users)):
        if user.id == user_id:
            del users[i]
            break
    return Response(status_code=204)


@user_router.put('/{user_id}', name='Обновить данные пользователя', response_model=UserSchema)
def update_user(user_id: int, new_user_data: UpdateUserSchema):
    for user in users:
        if user.id == user_id:
            data = new_user_data.dict()
            for key in data:
                if data[key] is not None:
                    setattr(user, key, data[key])

            return user

    raise HTTPException(status_code=404, detail='User not found')

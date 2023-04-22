import asyncio
import logging

from sqlalchemy.exc import SQLAlchemyError

from db import User
from db.engine import SessionManager

logger = logging.getLogger(__name__)

async def _create_user(username: str, age: int):
    async_session = SessionManager().get_session()
    async with async_session:
        try:
            user = User(username=username, age=age)
            async_session.add(user)
            await async_session.commit()
        except(SQLAlchemyError) as exc:
            await async_session.rollback()
            logger.error('Get sqlachemy error')
            raise exc
        finally:
            await async_session.close()


def create_user_fon(username: str, age: int):
    asyncio.run(_create_user(username, age))

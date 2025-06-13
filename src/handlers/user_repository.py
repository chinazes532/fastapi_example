from sqlalchemy.ext.asyncio import AsyncSession

from src.db.database import async_session
from src.db.models import User
from sqlalchemy import select

from src.schemas.user import UserSchema


class RepositoryUser:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def set_user(self, creds: UserSchema):
        async with async_session() as session:
            user = User(name=creds.name,
                        age=creds.age)
            session.add(user)
            await session.commit()
            return user.id

    async def get_users(self):
        async with async_session() as session:
            users = await session.scalars(select(User))
            return users

    async def get_user(self, id: int):
        async with async_session() as session:
            user = await session.scalar(
                select(User).where(User.id == id)
            )
            return user





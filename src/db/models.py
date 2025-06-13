from typing import Annotated

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from src.db.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]


class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declared_attr
import os

import secrets
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column



PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://user:password@localhost:5432/blog"

async_engine = create_async_engine(PG_CONN_URI, echo=True)

Session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False
    )


class Base(DeclarativeBase):
    metadata=MetaData(
       naming_convention={
           "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_N_name)s",
            "ck": "ck_%(table_name)s_`%(constraint_name)s`",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s"
       }, 
    )

    @declared_attr.directive
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)

def generate_ref_code():
    return secrets.token_urlsafe(12).lower()


class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str | None] = mapped_column(unique=True)
    posts: Mapped[list["Post"]] = relationship(back_populates="user")

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"username={self.name!r}, "
            f"email={self.email!r}"
            ")"
        )


class Post(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String)
    published_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=False))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    body: Mapped[str | None] = mapped_column(String, unique=True)
    user: Mapped["User"] = relationship(back_populates="posts")

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"title={self.title!r}, "
            f"user_id={self.user_id!r}"
            ")"
        )
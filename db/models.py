import sqlalchemy as sql
import sqlalchemy.orm as orm
import sqlalchemy.orm.exc as orm_exc
import sqlalchemy.exc as sql_exc
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


class Base(orm.DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]
    passwd_hash: Mapped[str]
    affiliation: Mapped[str]
    ts_created: Mapped[datetime]
    ts_edited: Mapped[datetime]
    is_active: Mapped[bool]

    @staticmethod
    def new(username, password, email, affiliation="N/A", is_active=True):
        from .auth import get_password_hash
        now = datetime.now()
        user = User(
            username=username,
            email=email,
            passwd_hash=get_password_hash(password),
            affiliation=affiliation,
            ts_created=now,
            ts_edited=now,
            is_active=is_active,
        )
        return user

    def __repr__(self):
        return f"<User id={self.id}, username={self.username}"



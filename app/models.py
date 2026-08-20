from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Text
from sqlalchemy import Float

from datetime import datetime

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        unique=True,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    password = Column(
        String,
        nullable=False
    )

    is_admin = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class Bot(Base):
    __tablename__ = "bots"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        nullable=False
    )

    bot_name = Column(
        String,
        nullable=False
    )

    bot_token = Column(
        Text,
        nullable=False
    )

    bot_username = Column(
        String,
        nullable=True
    )

    status = Column(
        String,
        default="stopped"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        nullable=False
    )

    plan_name = Column(
        String,
        nullable=False
    )

    amount = Column(
        Float,
        nullable=False
    )

    expires_at = Column(
        DateTime,
        nullable=True
    )

    active = Column(
        Boolean,
        default=False
    )


class Payment(Base):
    __tablename__ = "payments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        nullable=False
    )

    order_id = Column(
        String,
        unique=True
    )

    payment_id = Column(
        String
    )

    amount = Column(
        Float
    )

    status = Column(
        String,
        default="PENDING"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
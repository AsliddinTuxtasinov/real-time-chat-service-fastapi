from uuid import uuid4

from sqlalchemy import (
    Column, String, DateTime, func, Boolean, ForeignKey, Text, UniqueConstraint
)

from chat_app.database import Base


class Room(Base):
    __tablename__ = "rooms"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()), unique=True)  # UUID as string
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # Timestamp when user is created

    name = Column(String, nullable=False)


class RoomMember(Base):
    __tablename__ = "room_members"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()), unique=True)  # UUID as string
    joined_at = Column(DateTime(timezone=True), server_default=func.now())  # Timestamp when user is created

    room_id = Column(String, ForeignKey("rooms.id"), nullable=False)
    user_id = Column(String)  # UUID as string

    # Ensure room_id and user_id combination is unique
    __table_args__ = (
        UniqueConstraint(room_id, user_id, name='room_members_unique'),
    )


class Message(Base):
    __tablename__ = "messages"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()), unique=True)  # UUID as string
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # Timestamp when user is created

    room_id = Column(String, ForeignKey("rooms.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(String)  # UUID as string
    message = Column(Text)

    is_read = Column(Boolean, default=False)

from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session

from chat_app.database import get_db
from chat_app.models.chat_models import Room, RoomMember, Message
from chat_app.schemas.chat_schemas import RoomSchema


class ChatOrmUtils:
    def __init__(self):
        self._rooms_table = Room
        self._room_members_table = RoomMember
        self._messages_table = Message

    def create_room_if_not_exists(self, data: RoomSchema, db_session: Session = Depends(get_db)):
        new_rooms = self._rooms_table(data)

        db_session.add(new_rooms)
        db_session.commit()
        db_session.refresh(new_rooms)

        return new_rooms

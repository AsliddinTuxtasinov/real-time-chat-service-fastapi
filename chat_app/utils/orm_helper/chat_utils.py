from sqlalchemy import func

from chat_app.models.chat_models import Room, RoomMember, Message
from chat_app.schemas.chat_schemas import RoomSchema, MessageSchema


class ChatUtils:
    def __init__(self, db_session):
        self._rooms_table = Room
        self._room_members_table = RoomMember
        self._messages_table = Message
        self._db_session = db_session

    def add_commit_refresh_db_data(self, entity):
        self._db_session.add(entity)
        self._db_session.commit()
        self._db_session.refresh(entity)
        return entity


class ChatRoomsUtils(ChatUtils):

    def create_room_if_not_exists(self, data: RoomSchema):
        new_room = self._rooms_table(**data.dict())
        return self.add_commit_refresh_db_data(entity=new_room)

    def get_rooms(self):
        return self._db_session.query(self._rooms_table).all()

    def get_incomplete_rooms(self):
        return (
            self._db_session.query(self._rooms_table)
            .join(self._room_members_table, self._rooms_table.id == self._room_members_table.room_id)
            .group_by(self._rooms_table.id)
            .having(func.count(RoomMember.id) == 1)
            .all()
        )

    def get_rooms_by_user_id(self, user_id):
        # Query to get all rooms the user is a member of
        return (
            self._db_session.query(self._rooms_table)
            .join(self._room_members_table, self._rooms_table.id == self._room_members_table.room_id)
            .filter(self._room_members_table.user_id == user_id)
            .all()
        )

    def join_room_if_not_exists_as_member(self, room_id, user_id):
        # Check if the user is already a member of the room
        existing_member = (
            self._db_session.query(self._room_members_table)
            .filter(self._room_members_table.user_id == user_id, self._room_members_table.room_id == room_id)
            .first()
        )

        if existing_member:
            return existing_member

        # if not existing member
        new_member = self._room_members_table(room_id=room_id, user_id=user_id)
        return self.add_commit_refresh_db_data(entity=new_member)


class ChatMessageUtils(ChatRoomsUtils):

    def create_message(self):
        pass

    def create_reply_message(self):
        pass

from chat_app.database import get_db
from chat_app.schemas.chat_schemas import RoomSchema
from chat_app.utils.orm_helper import ChatRoomsUtils, ChatMessageUtils

chat_room_orm_utils = ChatRoomsUtils(db_session=get_db())
chat_message_orm_utils = ChatMessageUtils(db_session=get_db())

# get all rooms
rooms = chat_room_orm_utils.get_rooms()
print(f"{rooms=}")

# create new room
new_room = chat_room_orm_utils.create_room_if_not_exists(data=RoomSchema(name="the_asliddin"))
print(f"{new_room=}")

# get joined room if exist else create room and get joined room
room_id, user_id = "room_id", "user_id"
joined_room = chat_room_orm_utils.join_room_if_not_exists_as_member(room_id=room_id, user_id=user_id)
print(f"{joined_room=}")

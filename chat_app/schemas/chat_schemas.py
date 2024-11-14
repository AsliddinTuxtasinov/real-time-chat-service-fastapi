from typing import Optional

from pydantic import BaseModel


class RoomSchema(BaseModel):
    name: Optional[str] = None  # Marking `name` as optional with a default value of None

    class Config:
        orm_mode = True  # Enables Pydantic to work with ORM objects directly
        from_attributes = True
        arbitrary_types_allowed = True  # This allows Pydantic to work with datetime


class RoomMemberSchema(BaseModel):
    room_id: str  # UUID as string, ForeignKey to Room
    user_id: str  # UUID as string, represents user ID

    class Config:
        orm_mode = True  # Enables Pydantic to work with ORM objects directly
        from_attributes = True
        arbitrary_types_allowed = True  # This allows Pydantic to work with datetime


class MessageSchema(BaseModel):
    room_id: str  # UUID as string, ForeignKey to Room
    user_id: str  # UUID as string, represents user ID
    message: str
    is_read: Optional[bool] = False

    class Config:
        orm_mode = True  # Enables Pydantic to work with ORM objects directly
        from_attributes = True
        arbitrary_types_allowed = True  # This allows Pydantic to work with datetime

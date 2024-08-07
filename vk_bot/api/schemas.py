from pydantic import BaseModel


class DefaultUserProfile(BaseModel):
    username: str
    platform: str
    role: str


class UserProfile(DefaultUserProfile):
    user_id: int

from typing import Optional

from pydantic import BaseModel


class DefaultUserProfile(BaseModel):
    username: str
    platform: str
    role: str


class UserProfile(DefaultUserProfile):
    user_id: int


class ContentOne(BaseModel):
    code_gift: Optional[str]
    url_gift: Optional[str]
    usefull_url: Optional[str]
    track_file: Optional[str]
    payment_url: Optional[str]
    help_install_file: Optional[str]
    # present_on_PK: str

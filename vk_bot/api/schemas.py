from pydantic import BaseModel


class PostResponse(BaseModel):
    status: int
    message: str


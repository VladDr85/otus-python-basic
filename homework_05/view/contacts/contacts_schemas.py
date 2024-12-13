from pydantic import BaseModel


class ContactIn(BaseModel):
    name: str
    phone: str
    email: str | None = None
    status: str | None = None
    city: str | None = None
from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional

class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birthday: datetime
    extra_data: Optional[str] = None

class UserCreate(ContactBase):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class User(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True
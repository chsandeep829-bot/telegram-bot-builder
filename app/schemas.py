from pydantic import BaseModel, EmailStr
from typing import Optional


class RegisterSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class LoginSchema(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True


class BotCreateSchema(BaseModel):
    name: str
    token: str


class PaymentCreateSchema(BaseModel):
    amount: float
    plan_name: str


class PaymentResponse(BaseModel):
    payment_url: str
    payment_id: str
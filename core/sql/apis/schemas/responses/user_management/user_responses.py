from typing import List
from pydantic import BaseModel


class RegisterResponse(BaseModel):
    access_token: str
    token_type: str


class LoginResponse(BaseModel):
    username: str
    email: str
    name: str
    access_token: str
    token_type: str


class UpdateUserResponse(BaseModel):
    username: str
    user_role: str
    user_role_id: str


class UserDetails(BaseModel):
    user_id: int
    password: str
    fullname: str
    username: str
    user_role: str
    user_role_id: int
    email_id: str

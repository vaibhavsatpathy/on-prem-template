from typing import List, Optional
from pydantic import BaseModel, Field


class Register(BaseModel):
    username: str = Field(..., description="Unique username")
    password: str
    fullname: str
    email_id: str = Field(None, description="User email Id")
    user_role: str = Field("editor", description="Role to be assigned to the user")
    user_role_id: int = Field(
        2, description="Role id: 1 for Admin, 2 for Editor, 3 for Viewer"
    )


class Login(BaseModel):
    username: str = Field(..., description="Username")
    password: str = Field(..., description="Password")


class UpdateUserRole(BaseModel):
    username: str = Field(..., description="Username")
    user_role: str


class ForgotPassword(BaseModel):
    username: str
    new_password: str


class UpdatePassword(BaseModel):
    username: str
    old_password: str
    new_password: str

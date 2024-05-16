from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sql import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    fullname = Column(String)
    password = Column(String)
    email_id = Column(String)
    user_role = Column(String)
    user_role_id = Column(Integer, ForeignKey("user_roles.user_role_id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

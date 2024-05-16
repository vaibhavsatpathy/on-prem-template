from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sql import Base


class Cloud(Base):
    __tablename__ = "cloud"
    __table_args__ = {"extend_existing": True}
    cloud_id = Column(Integer, primary_key=True)
    cloud_name = Column(String)

from sqlalchemy import Column, String, DateTime
from sql import Base


class AppConfig(Base):
    __tablename__ = "app_config"
    __table_args__ = {"extend_existing": True}
    config_parameter = Column(String, primary_key=True)
    config_value = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

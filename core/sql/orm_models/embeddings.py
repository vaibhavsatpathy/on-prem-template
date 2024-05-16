from sqlalchemy import Column, String, DateTime, Integer
from pgvector.sqlalchemy import Vector
from sql import Base


class Embeddings(Base):
    __tablename__ = "embeddings"
    __table_args__ = {"extend_existing": True}
    id = Column(String, primary_key=True)
    text = Column(String)
    embeddings = Column(Vector(3))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

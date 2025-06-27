from sqlalchemy import Column, DateTime, Integer, String, Text
from datetime import datetime
from .base import Base
class TimestampMixin:
    """
    Adds automatic created_at and updated_at timestamps.
    """
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow 
    )
class Post(TimestampMixin, Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    body = Column(Text, nullable=False)
from sqlalchemy import (
    Column, Integer, String, Boolean,
    Text, ForeignKey
)
from sqlalchemy.orm import relationship
from .base import Base
from .mixins import TimestampMixin
from .base import Session

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    is_published = Column(Boolean, default=False)
    def publish(self):
        """
        Mark post as published and save to DB.
        Raises ValueError if already published.
        """
        if self.is_published:
            raise ValueError("Post is already published.")
        self.is_published = True
        session = Session.object_session(self)  
        session.add(self)
        session.commit()
def __repr__(self):
    return f"<Post id={self.id} title={self.title!r}>"
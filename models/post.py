from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from .base import Base
from .mixins import TimestampMixin
from .association import post_tags

class Post(Base, TimestampMixin):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    body = Column(Text, nullable=False)
    is_published = Column(Boolean, default=False, nullable=False)
    
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    author = relationship('User', back_populates='posts')
    
    tags = relationship('Tag', secondary=post_tags, back_populates='posts')

    def publish(self):
        if self.is_published:
            raise ValueError("Post is already published.")
        self.is_published = True

    def unpublish(self):
        if not self.is_published:
            raise ValueError("Post is already a draft.")
        self.is_published = False

    def __repr__(self):
        return f"<Post id={self.id} title={self.title!r}>"

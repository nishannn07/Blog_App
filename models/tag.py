from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .mixins import TimestampMixin
from .association import post_tags

class Tag(Base, TimestampMixin):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    posts = relationship('Post', secondary=post_tags, back_populates='tags')

    def __repr__(self):
        return f'<Tag {self.name}>'

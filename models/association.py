from sqlalchemy import Table, Column, Integer, ForeignKey, String
from .base import Base
from sqlalchemy.orm import relationship
post_tags = Table(
    'post_tags', Base.metadata,
    Column('post_id', ForeignKey('posts.id'), primary_key=True),
    Column('tag_id', ForeignKey('tags.id'), primary_key=True)
)
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title= Column(String)
    tags = relationship('Tag', secondary=post_tags, back_populates='posts')

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    posts= relationship('Post', secondary=post_tags, back_populates='tags')
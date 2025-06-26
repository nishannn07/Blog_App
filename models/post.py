from project.app import db
from .mixins import TimestampMixin
from .association import post_tags
from sqlalchemy.orm import relationship

class Post(db.Model, TimestampMixin):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    body = db.Column(db.Text, nullable=False)
    is_published = db.Column(db.Boolean, default=False, nullable=False)
    
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    author = relationship('User', back_populates='posts')
    
    tags = relationship('Tag', secondary=post_tags, back_populates='posts')

    def publish(self):
        """Mark post as published and save to DB."""
        if self.is_published:
            raise ValueError("Post is already published.")
        self.is_published = True
        db.session.add(self)
        db.session.commit()

    def unpublish(self):
        """Mark post as a draft and save to DB."""
        if not self.is_published:
            raise ValueError("Post is already a draft.")
        self.is_published = False
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Post id={self.id} title={self.title!r}>"
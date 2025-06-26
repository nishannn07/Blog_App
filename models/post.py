import base
import association

class Post(base.Base):
    __table__ = 'posts'
    id = base.Column(base.Integer, primary_key=True)
    title = base.Column(base.String)
    body = base.Column(base.String)
    is_published = base.Column(base.Boolean)
    author_id = base.Column(base.Integer)
    tags = base.relationship('Tag', secondary=association.post_tags, back_populates='posts')






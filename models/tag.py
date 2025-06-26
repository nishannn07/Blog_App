import base
import association

class Tag(base.Base):
    id = base.Column(base.Integer, primary_key=True)
    name = base.Column(base.String)
    posts= base.relationship('Post', secondary=association.post_tags, back_populates='tags')


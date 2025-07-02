from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
    
    @classmethod
    def userNameExits(cls, username)->bool:
        return db.session.query(cls).filter_by(username = username) is not None
    
    @classmethod
    def emailExits(cls, email):
        return db.session.query(cls).filter_by(email = email).first() is not None
    
    @classmethod
    def validate(cls, email, password):
        return db.session.query(cls).filter_by(email = email, password = password).first() is not None


post_tags = db.Table('post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    content = db.Column(db.Text)
    is_published = db.Column(db.Boolean, nullable=False, default=True)
    is_deleted = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tags = db.relationship('Tag', secondary=post_tags, backref='posts')

    @classmethod
    def set_published(cls, id, value):
        db.session.query(cls).filter_by(id=id).update({'is_published' : value})
        db.session.commit()

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, default='post')


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    token = db.Column(db.Integer)
    
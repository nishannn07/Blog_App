
from flask import flash, redirect, url_for
from model.models import *
from flask import jsonify


def search(text, name):
    text = text.lower()
    name = name.lower()
    if name == 'all':
        return Post.query.filter_by(is_deleted=False, is_published=True)
    if name == 'author':
        return Post.query.filter().join(Post.author).filter(User.username.ilike(f"%{text}%"), Post.is_deleted==False, Post.is_published==True).all()
    if name == 'tags':
        return Post.query.join(Post.tags).filter(Tag.name.ilike(f"%{text}%")).all()
    return Post.query.filter(Post.is_deleted == False, Post.is_published == True, getattr(Post, name).ilike(f"%{text}%")).all()

def all_post():
    return Post.query.filter_by(is_deleted=False, is_published=True)

def list_posts(user_id):
    # user = User.query.get_or_404(user_id)
    return Post.query.filter_by(user_id=user_id,is_deleted=False, is_published=True).all()
    # return user.posts
    # return user.posts.filter_by(is_deleted=False).all()
    # posts = user.posts
    # return jsonify([{
    #     "id": post.id,
    #     "title": post.title,
    #     "content": post.content
    # } for post in posts])

def list_draft(user_id):
    return Post.query.filter_by(user_id=user_id, is_deleted=False, is_published=False).all()

def get_post(post_id):
    return Post.query.get_or_404(post_id)

def create_post(form):
    pass

def update_post(post_id, form):
    post = Post.query.get_or_404(post_id)
    
    post.title = form.title.data
    post.content = form.post.data

    for name in [form.tag1.data, form.tag2.data, form.tag3.data]:
        if name:
            tag = getOrCreateTag(name)
            post.tags.append(tag)

    db.session.commit()


def delete_post(post_id):
    pass

def save_draft(post_id):
    Post.set_published(post_id, True)

def getOrCreateTag(name):
    tag = Tag.query.filter_by(name=name.lower()).first()
    if not tag:
        tag = Tag(name=name.lower())
        db.session.add(tag)
    return tag
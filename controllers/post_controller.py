from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.post import Post
from models.tag import Tag
from flask import flash, redirect, url_for
engine = create_engine('sqlite:///blog.db')
Session = sessionmaker(bind=engine)

def list_posts(published=True):
    session = Session()
    posts = session.query(Post).filter_by(is_published=published).all()
    session.close()
    return posts

def get_post(post_id):
    session = Session()
    post = session.query(Post).get(post_id)
    session.close()
    return post

def create_post(form):
    session = Session()
    new_post = Post(
        title=form.title.data,
        body=form.body.data,
        is_published=form.is_published.data,
        author_id=1 
    )
    session.add(new_post)
    session.commit()
    session.close()
    flash('Successfull', 'success')
    return redirect(url_for('posts.show_posts'))

def update_post(post_id, form):
    session = Session()
    post = session.query(Post).get(post_id)
    if post:
        post.title = form.title.data
        post.body = form.body.data
        post.is_published = form.is_published.data
        session.commit()
        flash('Succesfull', 'success')
    else:
        flash('Post not found!', 'danger')
    session.close()
    return redirect(url_for('posts.post_detail', post_id=post_id))

def delete_post(post_id):
    session = Session()
    post = session.query(Post).get(post_id)
    if post:
        session.delete(post)
        session.commit()
        flash('Successfull', 'success')
    else:
        flash('Post not found!', 'danger')
    session.close()
    return redirect(url_for('posts.show_posts'))

def list_drafts():
    return list_posts(published=False)
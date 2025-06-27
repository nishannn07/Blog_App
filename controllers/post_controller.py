from models.base import Session
from models.post import Post
from models.tag import Tag
from flask import flash, redirect, url_for

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
        title=form['title'],
        body=form['body'],
        is_published='is_published' in form,
        author_id=1
    )
    session.add(new_post)
    session.commit()
    session.close()
    flash('Successful', 'success')
    return redirect(url_for('posts.show_posts'))


def update_post(post_id, form):
    session = Session()
    post = session.query(Post).get(post_id)
    if post:
        post.title = form['title']
        post.body = form['body']
        post.is_published = 'is_published' in form
        session.commit()
        flash('Successful', 'success')
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
        flash('Successful', 'success')
    else:
        flash('Post not found!', 'danger')
    session.close()
    return redirect(url_for('posts.show_posts'))

def list_drafts():
    return list_posts(published=False)
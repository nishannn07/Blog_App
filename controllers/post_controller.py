from project.app import db
from models.post import Post
from models.tag import Tag
from flask import flash, redirect, url_for

def list_posts(published=True):
    return Post.query.filter_by(is_published=published).all()

def get_post(post_id):
    return Post.query.get_or_404(post_id)

def create_post(form):
    new_post = Post(
        title=form.title.data,
        body=form.body.data,
        is_published=form.is_published.data,
    )
    db.session.add(new_post)
    db.session.commit()
    flash('Post created successfully!', 'success')
    return redirect(url_for('posts.show_posts'))

def update_post(post, form):
    post.title = form.title.data
    post.body = form.body.data
    post.is_published = form.is_published.data
    db.session.commit()
    flash('Post updated successfully!', 'success')
    return redirect(url_for('posts.post_detail', post_id=post.id))

def delete_post(post_id):
    post = get_post(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('posts.show_posts'))

def list_drafts():
    return list_posts(published=False)
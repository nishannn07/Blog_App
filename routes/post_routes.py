from flask import render_template, request, redirect, url_for, Blueprint, flash
from controllers.post_controller import (
    list_posts, get_post, create_post, update_post, list_drafts
)
post_bp=Blueprint('posts', __name__, url_prefix='/posts')


@post_bp.route('/',methods=['GET'])
def show_posts():
    posts= list_posts(published=True)
    if not posts:
        flash("No posts found")
    return render_template('posts.html', posts=posts)


@post_bp.route('/<int:post_id>', methods=['GET'])
def post_detail(post_id):
    posts=get_post(post_id)
    return render_template('post_detail.html', post=posts)


@post_bp.route('/new',methods=['GET','POST'])
def new_post():
    if request.method=='POST':
        return create_post(request.form)
    return render_template('post_form.html')


@post_bp.route('/<int:post_id>/edit',methods=['GET','POST'])
def edit_post(post_id):
    if request.method=='POST':
        return update_post(post_id,request.form)
    post = get_post(post_id)
    return render_template('post_form.html', post=post)

@post_bp.route('/drafts',methods=['GET'])
def drafts():
    post=list_drafts()
    return render_template("posts.html",post=post)

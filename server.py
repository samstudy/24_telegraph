from datetime import datetime
from flask import Flask, 
render_template, session, redirect, url_for, escape, request
from init import app, db
from model import Post


def get_user_hash():
    user_hash = request.cookies.get('user_hash')
    if user_hash:
        return user_hash
    else:
        user_hash = str(datetime.today().microsecond)
        return user_hash


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/post/<url_id>', methods=['GET'])
def post(url_id):
    post = Post.query.filter_by(url_id=url_id).first()
    owner_hash = get_user_hash()
    if post.user_hash == owner_hash:
        return render_template('edit.html', post=post)
    else:
        return render_template('post.html', post=post)


@app.route('/create', methods=['POST'])
def create():
    user_hash = get_user_hash()
    header = request.form['header']
    signature = request.form['signature']
    body = request.form['body']
    url_id = datetime.today().microsecond
    post = Post(header, signature, body, url_id, user_hash)
    db.session.add(post)
    db.session.commit()
    response = make_response(redirect(url_for('post',
                                              url_id=url_id)))
    response.set_cookie('user_hash', user_hash)
    return response


@app.route('/edit/<url_id>', methods=['POST'])
def edit(url_id):
    post = Post.query.filter_by(url_id=url_id).first()
    post.header = request.form['header']
    post.signature = request.form['signature']
    post.body = request.form['body']
    post.url_id = url_id
    user_hash = get_user_hash()
    post = Post(post.header, post.signature, post.body,
                url_id, user_hash)
    db.session.commit()
    return redirect(url_for('post',url_id=post.url_id))


if __name__ == "__main__":
    app.run(debug=True)

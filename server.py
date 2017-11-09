from flask import Flask, render_template, session, redirect, url_for, escape, request
from flask import make_response
from init import app, db
from model import Posts
from datetime import datetime



@app.route('/')
def form():
    return render_template('form.html')


@app.route('/post/<url_id>',methods=['GET'])
def post(url_id):
    post = Posts.query.filter_by(url_id = url_id).first()
    if request.cookies.get('url_id'):
        return render_template('edit.html',post = post)
    else:
        return render_template('post.html',post = post)
    


@app.route('/create', methods=['POST'])
def create():
    header = request.form['header']
    signature = request.form['signature']
    body = request.form['body']
    url_id = request.cookies['urlId']
    post = Posts(header, signature, body, url_id)
    db.session.add(post)
    db.session.commit()
    response = make_response(redirect(url_for('post',url_id = url_id)))
    response.set_cookie('url_id', url_id)
    return response



@app.route('/edit/<url_id>', methods=['POST'])
def edit(url_id):
    post = Posts.query.filter_by(url_id = url_id).first()
    post.header = request.form['header']
    post.signature = request.form['signature']
    post.body = request.form['body']
    post.url_id = url_id
    post = Posts(post.header, post.signature, post.body,url_id)
    db.session.commit()
    return redirect(url_for('post',url_id = post.url_id))



if __name__ == "__main__":
    app.run()

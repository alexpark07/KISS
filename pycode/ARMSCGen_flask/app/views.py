from app import app
from flask import render_template, flash, redirect, session, url_for, request, g

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = 'Home', user = user, posts = posts)

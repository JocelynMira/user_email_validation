from flask_app import app
from flask import render_template, redirect, request, flash
from flask_app.models.user_model import User


@app.route('/')
def index ():
    return render_template ('user_login.html')

@app.route('/new_user', methods = ['POST'])
def new_user():
    # data = {
    #     'first_name' : request.form['first_name'],
    #     'last_name' : request.form['last_name'],
    #     'email' : request.form['email']
    # }
    if not User.validate_user(request.form):
        return redirect ('/')
    User.save(request.form)
    return redirect ('/dashboard')


@app.route('/delete_user/<int:id>')
def delete_user(id):
    User.delete(id)
    return redirect ('/dashboard')


@app.route('/dashboard')
def all_users():
    return render_template ('show_users.html', users = User.show_all())

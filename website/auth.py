from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

# routes are here

auth = Blueprint('auth',__name__)

@auth.route('/login', methods = ['GET','POST'])


def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')


    return render_template("login.html")

@auth.route('/logout')

def logout():
    return render_template ('logout.html')

@auth.route('/register', methods = ['GET','POST'])

def register():
    if request.method =='POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
    # Check no user already exists with this email
        user = User.query.filter_by(email = email).first()
        if user:
            flash('User already exists', category = 'error')

    # Check Valid
        elif len(email)<4:
            flash('Email must be a real email address greater than 4 characters', category = 'error')
        elif len(name)<2:
            flash('Name must be greater than 1 characters', category = 'error')
        elif password1 != password2:
            flash('Passwords must be the same', category = 'error')
        elif len(password1) <5:
            flash('Password must greater than 4 characters', category = 'error')
        else:
            new_user = User(email=email, name=name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
         #   login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    return render_template ('register.html')
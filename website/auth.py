from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash

# routes are here

auth = Blueprint('auth',__name__)

@auth.route('/login', methods = ['GET','POST'])

def login():
    data = request.form
    
    return render_template ('login.html', data = data)

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
    # Check Valid
        if len(email)<4:
            flash('Email must be a real email address greater than 4 characters', category = 'error')
        elif len(name)<2:
            flash('Name must be greater than 1 characters', category = 'error')
        elif password1 != password2:
            flash('Passwords must be the same', category = 'error')
        elif len(password1) <5:
            flash('Password must greater than 4 characters', category = 'error')
        else:
            flash('Account Created', category = 'success')
            #add to database
    return render_template ('register.html')
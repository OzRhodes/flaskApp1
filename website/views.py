from flask import Blueprint
from flask import render_template
from flask import url_for


# routes are here

views = Blueprint('views',__name__)

@views.route('/')

def home():
    return render_template ('home.html')
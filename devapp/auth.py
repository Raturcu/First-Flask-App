from flask import Blueprint
from flask import render_template

auth = Blueprint('authh', __name__)

@auth.route('/')
def home():
    return render_template('login.html')



@auth.route('/register')
def register():
    return render_template('register.html')
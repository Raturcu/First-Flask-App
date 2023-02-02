from flask import Blueprint
from flask import render_template,request
from flask import flash

auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
    return render_template('login.html')



@auth.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        username=request.form.get('username')
        email=request.form.get('email')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        
        if len(str(username)) < 3:
            flash("Username must contains at least 4 characters!",category='error')
        elif len(str(email)) < 5:
            flash("Email adress must contains at least 5 characters!",category='error')
        elif password1 != password2:
            flash("Password don't match",category='error')
        elif len(str(password1))< 8:
            flash("Password must be at least 8 characters",category='error')
        else:
            flash('Account Created!',category='success')
        
   
    return render_template('register.html')
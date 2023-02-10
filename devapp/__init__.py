from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


db=SQLAlchemy();
DB_NAME="databse.db"

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='asdljhkh qlweqoiweu'
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///database.db'
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/views')
    app.register_blueprint(auth, url_prefix='/auth')
    
    from .models import Users,Notes
    
    
    
    return app

def create_database(app):
    if not path.exists('devapp/'):
       with app.app_context:
        db.create_all()
        print("Created Database!")

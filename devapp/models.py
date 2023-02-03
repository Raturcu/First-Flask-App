from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func 
import sqlalchemy_orm import Model

#type: ignore
Base=Model();

class Notes(db.Model):
    
    id=db.Column(db.Integer,primary_key=True)
    data=db.Column(db.String(1000))
    date=db.Column(db.DateTime(timezone=True),default=func.now())
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))

class Users(db.Model,UserMixin):
     
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(150))
    email=db.Column(db.String(150),unique=True)
    password=db.Column(db.String(150))
    #notes=db.Relationship('Notes')
    
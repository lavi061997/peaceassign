from db import db
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    company_name = db.Column(db.String(80))
    city = db.Column(db.String(80))
    state = db.Column(db.String(80))
    age = db.Column(db.Integer)
    website = db.Column(db.String(80), unique=True, nullable=False)				
    email = db.Column(db.String(80), unique=True, nullable=False)				
    zip = db.Column(db.Integer)
    			

    def __init__(self, id, first_name, last_name, company_name, city, state, zip, website, email, age):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.city = city
        self.state = state
        self.zip = zip
        self.email = email
        self.website = website
        self.age = age

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
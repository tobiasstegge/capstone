import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy.sql.schema import PrimaryKeyConstraint

from sqlalchemy.sql.sqltypes import Date

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Model Customer
    Defines Table Customer
'''
class Customer(db.Model):
  __tablename__ = 'Costumers'

  id = Column(Integer, primary_key=True)
  first_name = Column(String)
  last_name = Column(String)
  address = Column(String)
  date_of_birth = Column(Date)
  recieve_newsletter = Column(bool)

  orders = db.relationship("Order")

# not complete yet
  def format(self):
    return {
    'id': self.id,
    'first_name': self.first_name,
    'last_name': self.last_name}


def insert(self):
  db.session.add(self)
  db.session.commit()

def update():
  db.session.commit()

def delete(self):
  db.session.delete(self)
  db.session.commit()

'''
Model Customer
    Defines Table Customer
'''
class Order(db.Model):
  __tablename__ = 'Orders'

  id = Column(Integer, primary_key=True)
  manufacturer = Column(String)
  name_long = Column(String)
  name_short = Column(String)
  molecules = Column(String)
  price = Column(float) 

'''
CRUD functions for DB interaction
  defines functions in model scope
'''
def insert(model):
  db.session.add(model)
  db.session.commit()

def update():
  db.session.commit()

def delete(model):
  db.session.delete(model)
  db.session.commit()




from os import curdir
from models import Customer, Order
import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS



def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app)

  return app

app = create_app()

## ROUTES

@app.route('/')
def get_test():
  return "API Working"

@app.route('/customers', methods=["GET"])
def get_all_customers():

  customers = Customer.query.all()

  return jsonify ({
    'success': True,
    'customers': [customer.format() for customer in customers]
  })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
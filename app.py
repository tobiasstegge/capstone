from os import curdir
from models import Customer, Order, setup_db
import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


def create_app(test_config=None):
  app = Flask(__name__)
  setup_db(app)
  CORS(app, resources={r"/*": {"origins": "*"}})

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
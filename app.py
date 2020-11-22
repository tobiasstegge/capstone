from os import curdir
from models import Customer, Order, setup_db
import os
from flask import Flask, request, abort, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import Customer, Order, setup_db
from auth import AuthError, requires_auth


def create_app(test_config=None):
  app = Flask(__name__)
  setup_db(app)
  CORS(app, resources={r"/*": {"origins": "*"}})

  return app

app = create_app()

### ROUTES ###

@app.route('/')
def get_test():
  return render_template('/home.html')


# CUSTOMERS #
@app.route('/customers', methods=['GET'])
@requires_auth('get:customer')
def get_all_customers(payload):

  customers = Customer.query.all()

  return jsonify ({
    'success': True,
    'customers': [customer.format() for customer in customers]
  })

@app.route('/customers', methods=['POST'])
@requires_auth('post:customer')
def post_new_customer(payload):

  body = request.get_json()

  first_name = body.get('first_name')
  last_name = body.get('last_name')
  address = body.get('address')

  if body.get('recieve_newsletter') == "true":
    recieve_newsletter = True
  else:
    recieve_newsletter = False

  new_customer = Customer(first_name=first_name, last_name=last_name, address=address, recieve_newsletter=recieve_newsletter)

  new_customer.insert()
  print("Inserted new customer")

  return jsonify ({
    'success': True,
    'customer': new_customer.format()
  })

@app.route('/customers/<int:id>', methods=['PATCH'])
@requires_auth('patch:customer')
def patch_customer(payload, id):

  customer = Customer.query.filter(Customer.id==id).one_or_none()

  if customer is None:
      abort(404)

  body = request.get_json()

  customer.first_name = body.get('first_name')
  customer.last_name = body.get('last_name')
  customer.address = body.get('address')

  if body.get('recieve_newsletter') == "true":
    customer.recieve_newsletter = True
  else:
    customer.recieve_newsletter = False

  customer.update()
  print('Updated customer')

  return jsonify({
      'success': True,
      'customer': [customer.format()]
  })

@app.route('/customers/<int:id>', methods=['DELETE'])
@requires_auth('delete:customer')
def delete_customer(payload, id):

    customer = Customer.query.filter(Customer.id==id).one_or_none()

    if customer is None:
        abort(404)

    customer.delete()
    print('Deleted customer')

    return jsonify({
        'success': True,
        'delete': id
    })


# ORDERS #
@app.route('/orders', methods=['GET'])
@requires_auth('get:order')
def get_all_orders(payload):

  orders = Order.query.all()

  return jsonify ({
    'success': True,
    'orders': [order.format() for order in orders]
  })

@app.route('/orders', methods=['POST'])
@requires_auth('post:order')
def post_new_order(payload):

  body = request.get_json()

  manufacturer = body.get('manufacturer')
  name = body.get('name')
  price = body.get('price')
  customer_id = body.get('customer_id')

  new_order = Order(manufacturer=manufacturer, name=name, price=price, customer_id=customer_id)

  new_order.insert()
  print("Inserted new order")

  return jsonify ({
    'success': True,
    'customer': new_order.format()
  })


### Error Handling ###

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 422,
                    "message": "unprocessable"
                    }), 422

@app.errorhandler(404)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 404,
                    "message": "resource not found"
                    }), 404

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
                  "success": False,
                   "error": 401,
                   "message": "unauthorized"
                   }), 401

@app.errorhandler(AuthError)
def auth_error(e):
    return jsonify({
        "success": False,
        "error": e.status_code,
        "message": str(e.error) + " (authentification fails)"
                    }), 401

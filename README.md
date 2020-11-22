# Capstone Project - Shop Backbone 

## About

This is the final project for dacity's Full Stack Web Development Nanodegree. It implements an examplary API for a shop with customers and orders. In a future development layout the data model and API endpoints should support more data and functionality, which is still to be implemented.

https://capstone-stegge.herokuapp.com

## Key Project Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM. As the underlying database a postgres will is used

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension used to handle cross origin requests from our frontend server. 

## Local Development Instructions

### Database Setup
For local setup run the backend folder in terminal:
```bash
createdb shop
```

### Running the server

Run the server from the correct directory, where app.py is located and enable the local virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to use the app.py application.


## API

To handle and store data, backend functionality is provided by an API. An overview of the API is given below. 

### Roles and Permissions

The shop API can be accessed by two differnt roles, that each have different permissions.

#### Admin
_An Admin is able to access every endpoint for testing and maintenance. He can manage data_

They have the following permissions:
* get:customer
* post:customer
* patch:customer
* delete:customer

* get:order
* post:order

#### User
_A User is able to just access a few endpoints for customer service actions. He can retrieve data_

They have the following permissions:
* get:customer

* get:order

## Endpoints

_Examples on how to use all endpoints can be found in the provided provided a [Postman Collection](https://github.com/tobiasstegge/capstone/blob/main/test-capstone-stegge.postman_collection.json)._

### Customers

**GET** '\customers'

Retrieve all the customers in the system.

**POST** '\customers'

Creates a new customer.

**Patch** '\customers\id'

Updates the data of an existing user under the given ID.

**DELETE** '\customers\id'

Deletes user with given ID.


### Orders

**GET** '\orders'

Retrieve all the orders in the system.

**POST** '\orders'

Creates a new order.

## Testing

### Local

To tests the API, run
```
createdb capstone_test
python test_app.py
```

### Heroku

For testing in Heroku the [Postman Collection](https://github.com/tobiasstegge/capstone/blob/main/test-capstone-stegge.postman_collection.json) can be used. Here the required JWT's can be found as a saved variable. 
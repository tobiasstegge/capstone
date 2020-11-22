import os
import unittest
import json

from flask_sqlalchemy import SQLAlchemy

from app import app
from models import db

JWT_ADMIN = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndaRFpKQTZpM2Vwd3dMeVE5X05pRyJ9.eyJpc3MiOiJodHRwczovL3NhdmVzdGVnZ2UuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmYmFiMWY3YWZkNzU5MDA2ZTIyYjgyMSIsImF1ZCI6Imh0dHBzOi8vY2Fwc3RvbmUtc3RlZ2dlLXRlc3QvIiwiaWF0IjoxNjA2MDcxMTI1LCJleHAiOjE2MDYxNTc1MjUsImF6cCI6Ik1SdjEwWkhjZmgxMjF5V0E3b3VwUWRwM1VJZDVDZTV1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Y3VzdG9tZXIiLCJnZXQ6Y3VzdG9tZXIiLCJnZXQ6b3JkZXIiLCJwYXRjaDpjdXN0b21lciIsInBvc3Q6Y3VzdG9tZXIiLCJwb3N0Om9yZGVyIl19.SQlarPNEwg7dfbY6rIPNg7TZ9C5fPZGIA_zs5TTQ_sABg0Cswfli24s_S4FffK29imJdLkxxDF4kzT7fg1BI6a4RhXtEn1gDJBMlVwPpTxkMmf9scO0fceyF8XVcPw67Hsb4Oc0K8j2IqVOkrxtGcy22QSq9p8G427BSreIht_Z7ItBqDpBq7vmN78TLFVuKYdX9Eoy34x0XSmK6wyba5zb153sO9hYqZe1aA-ib_L7P8n1E1-4M6vvqHgMRJfJ7VleUBRJvVP3nII1ZDGqdkxt1ockXaC9V_EFhf7zlu7zSLlpDdIN4cmrsg_jAv7RmA4Lh-_cmDdTwTJVhDTFO2g'

JWT_USER = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndaRFpKQTZpM2Vwd3dMeVE5X05pRyJ9.eyJpc3MiOiJodHRwczovL3NhdmVzdGVnZ2UuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmYmFiODNlNDQ4OTRhMDA2ODA0NmI2NiIsImF1ZCI6Imh0dHBzOi8vY2Fwc3RvbmUtc3RlZ2dlLXRlc3QvIiwiaWF0IjoxNjA2MDcyNDQ4LCJleHAiOjE2MDYxNTg4NDgsImF6cCI6Ik1SdjEwWkhjZmgxMjF5V0E3b3VwUWRwM1VJZDVDZTV1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6Y3VzdG9tZXIiLCJnZXQ6b3JkZXIiXX0.VKQ-xnmo6W0Hbe4c62F4yfZ_foX7s0e3EoZnqc8dVNMnEVUFX1HRN7xCitOEjG6juTJBf2keflbOGlfmeU2Kau6dsF_Rl56i8R_yGWCZ_EpbQsc4w_cdcJtQYax_ymz4Phhazdop3UMTYMr5a84mFQGRtIzb6qWm5jVXjGT6Yl3ADAglyj93FTtmfpCbDwVWqgIcgYDUaNqZsXlvJ5MeHiu_g3rdFVbNTtuB3BQmPu1f6kJS6z69twvfJKq8r3tl57ZdY96y-bfXG-FcHdAxd70XUzIbBs6PiltkLdYLbquHNLeaVDu9nEkVbfaQc9LJtcGFC4SttwbTHvH4BvORGA'

class TestCase(unittest.TestCase):

  ### SETUP ###
  def setUp(self):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tobiassteggemann1@localhost:5432/shop'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    self.client = app.test_client()
    
    db.drop_all()
    db.create_all()

    self.header_user = {
      'Content-Type': 'application/json',
      'Authorization': JWT_USER
    }

    self.header_admin = {
      'Content-Type': 'application/json',
      'Authorization': JWT_ADMIN
    }

    self.new_customer = {
      "first_name": "Tobi",
      "last_name": "Steggemann",
      "address": "Test Post, 62, Bremen",
      "recieve_newsletter": True 
    }

    self.new_order = {
      "manufacturer": "healthtec",
      "name": "Gute Pille",
      "price": 19.99,
      "customer_id": 1
    }

  def tearDown(self):
     pass


  ### TESTS ADMIN ###
  def test_get_customers(self):
    res = self.client.get('/customers', headers=self.header_admin)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)

  def test_get_orders(self):
    res = self.client.get('/orders', headers=self.header_admin)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)

  def test_post_customers(self):
    res = self.client.post('/customers',json=self.new_customer, headers=self.header_admin)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)

  def test_post_order(self):
    self.client.post('/customers',json=self.new_customer, headers=self.header_admin)
    res = self.client.post('/orders',json=self.new_order, headers=self.header_admin)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)

  def test_patch_customers(self):
    self.client.post('/customers',json=self.new_customer, headers=self.header_admin)
    res = self.client.patch('/customers/1',json=self.new_customer, headers=self.header_admin)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
  
  def test_delete_customers(self):
    self.client.post('/customers',json=self.new_customer, headers=self.header_admin)
    res = self.client.delete('/customers/1', headers=self.header_admin)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)

  ### TESTS USER ###
  def test_get_customers_user(self):
    res = self.client.get('/customers', headers=self.header_user)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)

  def test_get_orders_user(self):
    res = self.client.get('/orders', headers=self.header_user)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)

  def test_post_customers_user(self):
    res = self.client.post('/customers',json=self.new_customer, headers=self.header_user)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 401)

  def test_post_order_user(self):
    self.client.post('/customers',json=self.new_customer, headers=self.header_user)
    res = self.client.post('/orders',json=self.new_order, headers=self.header_user)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 401)

  def test_patch_customers_user(self):
    self.client.post('/customers',json=self.new_customer, headers=self.header_user)
    res = self.client.patch('/customers/1',json=self.new_customer, headers=self.header_user)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 401)
  
  def test_delete_customers_user(self):
    self.client.post('/customers',json=self.new_customer, headers=self.header_user)
    res = self.client.delete('/customers/1', headers=self.header_user)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 401)


# Execute tests
if __name__ == "__main__":
    unittest.main()
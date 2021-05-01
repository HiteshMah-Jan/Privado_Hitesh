
from django.test import TestCase
from django.test import Client

class GetTest(TestCase):
    @classmethod
    def setUpClass(self):
        # creating instance of a client.
        self.client = Client()

    def test_home(self):
        response = self.client.get('http://127.0.0.1:8000')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_access_existing_customer_info(self):
        response = self.client.get('http://127.0.0.1:8000/te/customer/1/templates/')
        self.assertEqual(response.status_code, 200)

    def test_customer_not_found(self):
        response = self.client.get('http://127.0.0.1:8000/te/customer/87/templates/')
        self.assertEqual(response.status_code, 200)

    def test_bad_customer_id(self):
        response = self.client.get('http://127.0.0.1:8000/te/customer/hitesh/templates/')
        self.assertEqual(response.status_code, 200)

    @classmethod
    def tearDownClass(cls):
        pass
    
# comment to test hook

class PostTest(TestCase):
    @classmethod
    def setUpClass(self):
        # creating instance of a client.
        self.client = Client()

    def test_create_instance_for_new_id(self):
        response = self.client.post('http://127.0.0.1:8000/te/customer/2/templates/')
        self.assertEqual(response.status_code, 200)

    def test_update_instance_for_existing_id(self):
        response = self.client.post('http://127.0.0.1:8000/te/customer/1/templates/')
        self.assertEqual(response.status_code, 200)

    def test_bad_customer_id(self):
        response = self.client.post('http://127.0.0.1:8000/te/customer/privado/templates/')
        self.assertEqual(response.status_code, 200)

    @classmethod
    def tearDownClass(cls):
        pass

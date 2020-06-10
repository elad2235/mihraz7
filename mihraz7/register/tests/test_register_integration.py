import os
import unittest
import django
django.setup()
from django.test import Client
from account.models import Account
os.environ['DJANGO_SETTINGS_MODULE'] = 'mihraz7.settings'


class TestingAccountsIntegration(unittest.TestCase):
    def test_register_login(self):
        account_instance = Account.objects.create_user(email='test_@test.com', username='test_', first_name='tes', last_name='ting', phone='111111111', password='testtest')
        account_instance.save()
        retrieve = Account.objects.get(username='test_')
        client = Client()
        response = client.post('/account/login_user/', {'username': 'test_', 'password': 'testtest'}, follow=True)
        self.assertEqual(response.status_code, 200)
        retrieve.delete()

    def test_register_login_custom_function_disconnect(self):
        account_instance = Account.objects.create_user(email='test_@test.com', username='test_', first_name='tes', last_name='ting', phone='111111111', password='testtest')
        account_instance.save()
        retrieve = Account.objects.get(username='test_')
        client = Client()
        response = client.post('/account/login_user/', {'username': 'test_', 'password': 'testtest'}, follow=True)
        self.assertEqual(response.status_code, 200)
        client.get('/account/logOut')
        response = client.get('/account/homePage')
        self.assertEqual(response.status_code, 301)
        retrieve.delete()

# Sprint 3 Revisioned:
    def test_register_form_login_disconnect(self):
        # Registration and Login stage
        client = Client()
        response = client.post('/register/', {'username': 'test_', 'password1': 'jy9vq7sqWPpMCLAD5Cof', 'password2': 'jy9vq7sqWPpMCLAD5Cof', 'phone': '2235', 'first_name': '_test_', 'last_name': '_test_', 'email': '_test_@test.com'}, follow=True)
        self.assertEqual(response.status_code, 200)
        retrieve = Account.objects.get(username='test_')
        # Disconnect Stage
        client.get('/account/logOut')
        response = client.get('/account/homePage')
        self.assertEqual(response.status_code, 301)
        # Cleanup
        retrieve.delete()

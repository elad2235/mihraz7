import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mihraz7.settings'
import unittest
import django
django.setup()
from django.test import Client
from account.models import Account


class TestingAccountsIntegration(unittest.TestCase):

    def test_add_delete(self):
        # Test Add and Delete Functions - mongo | pymongo | djongo
        account_instance = Account.objects.create_user(email='test_@test.com', username='test_', first_name='tes', last_name='ting', phone='111111111', password='testtest')
        account_instance.save()
        retrieve = Account.objects.get(username='test_')
        account_instance.delete()
        self.assertNotEqual(None, retrieve.last_name)

    def test_connect_disconnect(self):
        # Test Login -> Disconnect page
        client = Client()
        client.post('/account/login_user/', {'username': 'TestMe', 'password': '1342'}, follow=True)
        client.get('/account/logOut')
        response = client.get('/account/homePage')
        self.assertEqual(response.status_code, 301)

    def test_admin_connect_add_user_disconnect(self):
        # Test Login -> use Add user Function -> disconnect page
        client = Client()
        client.post('/account/login_user/', {'username': 'TestMe', 'password': '1342'}, follow=True)
        account_instance = Account.objects.create_user(email='test_@test.com', username='test_', first_name='tes', last_name='ting', phone='111111111', password='testtest')
        account_instance.save()
        retrieve = Account.objects.get(username='test_')
        account_instance.delete()
        self.assertNotEqual(None, retrieve.last_name)
        client.get('/account/logOut')
        response = client.get('/account/homePage')
        self.assertEqual(response.status_code, 301)

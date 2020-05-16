import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mihraz7.settings'
import unittest
import django
import xmlrunner
django.setup()

from django.test import Client
from account.models import Account


class TestingAccountsIntegration(unittest.TestCase):
    def test_add_delete(self):
        account_instance = Account.objects.create_user(email='test_@test.com',username='test_',first_name='tes',last_name='ting',phone='111111111',password='testtest')
        account_instance.save()
        retrieve = Account.objects.get(username='test_')
        account_instance.delete()
        self.assertNotEqual(None, retrieve.last_name)


    def test_connect_disconnect(self):
        client = Client()
        client.post('/account/login_user/',{'username':'TestMe','password':'1342'},follow=True)
        client.get('/account/logOut')
        response = client.get('/account/homePage')
        self.assertEqual(response.status_code, 301)

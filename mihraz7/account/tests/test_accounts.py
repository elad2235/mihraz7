import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mihraz7.settings'
import unittest
import django
django.setup()
import xmlrunner
from account.models import Account
from django.test import Client
from account.views import login_user
from django.urls import reverse, resolve


class TestingAccounts(unittest.TestCase):
    def test_admin_login(self):
        client = Client()
        response = client.post('/account/login_user/', {'username': 'TestMe', 'password': '1342'}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_user_login(self):
        account_instance = Account.objects.create_user(email='test_@test.com', username='test_', first_name='tes', last_name='ting', phone='111111111', password='testtest')
        account_instance.save()
        retrieve = Account.objects.get(username='test_')
        client = Client()
        response = client.post('/account/login_user/', {'username': 'test_', 'password': 'testtest'}, follow=True)
        self.assertEqual(response.status_code, 200)
        retrieve.delete()

    def test_bad_credentials(self):
        client = Client()
        response = client.post('/account/login_user/', {'username': 'Tessadt|Me', 'password': ''})
        self.assertEqual(response.status_code, 401)

    def test_admin_disconnect(self):
        client = Client()
        client.post('/account/login_user/', {'username': 'TestMe', 'password': '1342'}, follow=True)
        client.get('/account/logOut')
        response = client.get('/account/homePage')
        self.assertEqual(response.status_code, 301)

    def test_user_disconnect(self):
        account_instance = Account.objects.create_user(email='test_@test.com', username='test_', first_name='tes', last_name='ting', phone='111111111', password='testtest')
        account_instance.save()
        retrieve = Account.objects.get(username='test_')
        client = Client()
        response = client.post('/account/login_user/', {'username': 'test_', 'password': 'testtest'}, follow=True)
        client.get('/account/logOut')
        response = client.get('/account/homePage')
        self.assertEqual(response.status_code, 301)
        retrieve.delete()

    def test_add_user(self):
        account_instance = Account.objects.create_user(email='test_@test.com', username='test_', first_name='tes', last_name='ting', phone='111111111', password='testtest')
        account_instance.save()
        retrieve = Account.objects.get(username='test_')
        self.assertEqual(account_instance.last_name, retrieve.last_name)
        retrieve.delete()

    def test_delete_user(self):
        account_instance = Account.objects.create_user(email='test_@test.com', username='test_', first_name='tes', last_name='ting', phone='111111111', password='testtest')
        account_instance.save()
        retrieve = Account.objects.get(username='test_')
        account_instance.delete()
        self.assertNotEqual(None, retrieve.last_name)
        retrieve.delete()

    def test_perm_isAdmin_true(self):
        account_instance = Account.objects.create_user(email='test_@test.com', username='test_', first_name='tes', last_name='ting', phone='111111111', password='testtest', is_admin=True)
        account_instance.save()
        retrieve = Account.objects.get(username='test_')
        account_instance.delete()
        self.assertEqual(True, retrieve.is_admin)
        retrieve.delete()

    def test_perm_isAdmin_false(self):
        account_instance = Account.objects.create_user(email='test_@test.com', username='test_', first_name='tes', last_name='ting', phone='111111111', password='testtest', is_admin=False)
        account_instance.save()
        retrieve = Account.objects.get(username='test_')
        account_instance.delete()
        self.assertEqual(False, retrieve.is_admin)
        retrieve.delete()

    def test_url_login(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login_user)

    def test_url_homepage(self):
        url = reverse('homePage')
        self.assertEqual(resolve(url).url_name, 'homePage')

    def test_url_account_logout(self):
        url = reverse('account_logout')
        self.assertEqual(resolve(url).url_name, 'account_logout')

    def test_url_tender(self):
        url = reverse('Tender')
        self.assertEqual(resolve(url).url_name, 'Tender')


if __name__ == '__main__':
    with open('test-reports/results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
# Admin user for testing
# TestMe
# testtestMihraz7@gmail.com
# TestingGeneraltest
# 123321
# 1342
# 1342

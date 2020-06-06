import os
from django.test import Client
import unittest
import django
django.setup()
import xmlrunner
os.environ['DJANGO_SETTINGS_MODULE'] = 'mihraz7.settings'


class TestingGeneral(unittest.TestCase):
    def test_admin_login(self):
        client = Client()
        response = client.post('/admin/', {'username': 'TestMe', 'password': '1342'}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_bad_credentials(self):
        client = Client()
        response = client.post('/admin/', {'username': 'Tessadt|Me', 'password': ''})
        self.assertNotEqual(response.status_code, 200)

    def test_disconnect(self):
        client = Client()
        client.post('/admin/', {'username': 'TestMe', 'password': '1342'}, follow=True)
        client.get('/admin/logout')
        response = client.get('/admin/account/account/')
        self.assertEqual(response.status_code, 302)


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

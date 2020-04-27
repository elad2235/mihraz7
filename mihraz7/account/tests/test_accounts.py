import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mihraz7.settings'
import unittest
import django
import xmlrunner
django.setup()

from django.test import Client

class TestingAccounts(unittest.TestCase):
    def test_admin_login(self):
        client = Client()
        response = client.post('/account/login_user/',{'username':'TestMe','password':'1342'},follow=True)
        self.assertEqual(response.status_code, 200)

    def test_bad_credentials(self):
        client = Client()
        response = client.post('/account/login_user/',{'username':'Tessadt|Me','password':''})
        self.assertEqual(response.status_code, 401)
        
    def test_disconnect(self):
        client = Client()
        client.post('/account/login_user/',{'username':'TestMe','password':'1342'},follow=True)
        client.get('/account/logOut')
        response = client.get('/account/homePage')
        self.assertEqual(response.status_code, 301)

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
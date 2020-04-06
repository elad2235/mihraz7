import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mihraz7.settings'
import unittest
import django
django.setup()

from django.test import Client

class TestingGeneral(unittest.TestCase):
    def test_admin_login(self):
        client = Client()
        response = client.post('/admin/',{'username':'TestMe','password':'1342'},follow=True)
        self.assertEqual(response.status_code, 200)


    def test_bad_credentials(self):
        client = Client()
        response = client.post('/admin/',{'username':'Tessadt|Me','password':''})
        self.assertNotEqual(response.status_code, 200)
        
    def test_disconnect(self):
        client = Client()
        client.post('/admin/',{'username':'TestMe','password':'1342'},follow=True)
        client.get('/admin/logout')
        response = client.get('/admin/account/account/')
        self.assertEqual(response.status_code, 302)


# Admin user for testing  
# TestMe
# testtestMihraz7@gmail.com
# TestingGeneraltest
# 123321
# 1342
# 1342
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mihraz7.settings'
import unittest
import django
django.setup()
from contact.models import contact


class TestingContactIntegration(unittest.TestCase):
    def test_add_delete_contact(self):
        contact_instance = contact.objects.create(Name='Test1', Email='Test@test.com', Subject='testing', Message='Hello', date='2020-05-17')
        contact_instance.save()
        retrieve = contact.objects.get(Name='Test1')
        contact_instance.delete()
        self.assertNotEqual(None, retrieve.Name)

import os
import unittest
import django
from contact.models import contact
os.environ['DJANGO_SETTINGS_MODULE'] = 'mihraz7.settings'
django.setup()


class TestingContactIntegration(unittest.TestCase):
    def test_add_delete_contact(self):
        contact_instance = contact.objects.create(Name='Test1', Email='Test@test.com', Subject='testing', Message='Hello', date='2020-05-17')
        contact_instance.save()
        retrieve = contact.objects.get(Name='Test1')
        contact_instance.delete()
        self.assertNotEqual(None, retrieve.Name)

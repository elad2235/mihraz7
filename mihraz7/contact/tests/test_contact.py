import os
import unittest
import django
django.setup()
import xmlrunner
from contact.models import contact
os.environ['DJANGO_SETTINGS_MODULE'] = 'mihraz7.settings'


class TestingContact(unittest.TestCase):

    def test_insert_name(self):
        contact_instance = contact.objects.create(Name='Test1', Email='Test@test.com', Subject='testing', Message='Hello', date='2020-05-17')
        contact_instance.save()
        retrieve = contact.objects.get(Name='Test1')
        self.assertEqual(contact_instance.Name, retrieve.Name)
        retrieve.delete()

    def test_insert_email(self):
        contact_instance = contact.objects.create(Name='Test1', Email='Test@test.com', Subject='testing', Message='Hello', date='2020-05-17')
        contact_instance.save()
        retrieve = contact.objects.get(Email='Test@test.com')
        self.assertEqual(contact_instance.Email, retrieve.Email)
        retrieve.delete()

    def test_insert_subject(self):
        contact_instance = contact.objects.create(Name='Test1', Email='Test@test.com', Subject='testing', Message='Hello', date='2020-05-17')
        contact_instance.save()
        retrieve = contact.objects.get(Subject='testing')
        self.assertEqual(contact_instance.Subject, retrieve.Subject)
        retrieve.delete()

    def test_insert_message(self):
        contact_instance = contact.objects.create(Name='Test1', Email='Test@test.com', Subject='testing', Message='Hello', date='2020-05-17')
        contact_instance.save()
        retrieve = contact.objects.get(Message='Hello')
        self.assertEqual(contact_instance.Message, retrieve.Message)
        retrieve.delete()

    def test_remove_contact(self):
        contact_instance = contact.objects.create(Name='Test1', Email='Test@test.com', Subject='testing', Message='Hello', date='2020-05-17')
        contact_instance.save()
        contact_instance.delete()
        try:
            retrieve = contact.objects.get(Name='Test1')
        except contact.DoesNotExist:
            retrieve = None
        self.assertEqual(None, retrieve)


if __name__ == '__main__':
    with open('test-reports/results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)

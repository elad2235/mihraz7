import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mihraz7.settings'
import unittest
import django
import xmlrunner
django.setup()
from account.models import Account

class TestingRegister(unittest.TestCase):
    
    def test_insert_email_field(self):
        account_instance = Account.objects.create_user(email='test_@test.com',username='test_',first_name='tes',last_name='ting',phone='111111111',password='testtest')
        account_instance.save()
        retrieve = Account.objects.get(username='test_')
        self.assertEqual(account_instance.email, retrieve.email)
        retrieve.delete()

    def test_insert_username_field(self):
        account_instance = Account.objects.create_user(email='test_@test.com',username='test_',first_name='tes',last_name='ting',phone='111111111',password='testtest')
        account_instance.save()
        retrieve = Account.objects.get(username='test_')
        self.assertEqual(account_instance.username, retrieve.username)
        retrieve.delete()


    def test_insert_first_name_field(self):
        account_instance = Account.objects.create_user(email='test_@test.com',username='test_',first_name='tes',last_name='ting',phone='111111111',password='testtest')
        account_instance.save()
        retrieve = Account.objects.get(username='test_')
        self.assertEqual(account_instance.first_name, retrieve.first_name)
        retrieve.delete()


    def test_insert_last_name_field(self):
        account_instance = Account.objects.create_user(email='test_@test.com',username='test_',first_name='tes',last_name='ting',phone='111111111',password='testtest')
        account_instance.save()
        retrieve = Account.objects.get(username='test_')
        self.assertEqual(account_instance.last_name, retrieve.last_name)
        retrieve.delete()


    def test_insert_phone_field(self):
        account_instance = Account.objects.create_user(email='test_@test.com',username='test_',first_name='tes',last_name='ting',phone='111111111',password='testtest')
        account_instance.save()
        retrieve = Account.objects.get(username='test_')
        self.assertEqual(account_instance.phone, retrieve.phone)
        retrieve.delete()

if __name__ == '__main__':
    with open('test-reports/results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
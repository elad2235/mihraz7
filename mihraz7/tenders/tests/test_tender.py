import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mihraz7.settings'
import unittest
import django
import xmlrunner
import datetime 
django.setup()

from tenders.models import Tender

class TestingTender(unittest.TestCase):
    
    def test_insert_tender_name(self):
        tender_instance = Tender.objects.create(tender_name='Tender1', tender_id='1234', winner='test1', files='file', online_payment='yes', url='test.com', end_date='2020-05-17', update_date='2020-05-14')
        tender_instance.save()
        retrieve = Tender.objects.get(tender_name='Tender1')
        self.assertEqual(tender_instance.tender_name, retrieve.tender_name)
        retrieve.delete()

    def test_insert_tender_id(self):
        tender_instance = Tender.objects.create(tender_name='Tender1', tender_id='1234', winner='test1', files='file', online_payment='yes', url='test.com', end_date='2020-05-17', update_date='2020-05-14')
        tender_instance.save()
        retrieve = Tender.objects.get(tender_id='1234')
        self.assertEqual(tender_instance.tender_id, retrieve.tender_id)
        retrieve.delete()
    
    def test_insert_winner(self):
        tender_instance = Tender.objects.create(tender_name='Tender1', tender_id='1234', winner='test1', files='file', online_payment='yes', url='test.com', end_date='2020-05-17', update_date='2020-05-14')
        tender_instance.save()
        retrieve = Tender.objects.get(winner='test1')
        self.assertEqual(tender_instance.winner, retrieve.winner)
        retrieve.delete()
    
    def test_insert_files(self):
        tender_instance = Tender.objects.create(tender_name='Tender1', tender_id='1234', winner='test1', files='file', online_payment='yes', url='test.com', end_date='2020-05-17', update_date='2020-05-14')
        tender_instance.save()
        retrieve = Tender.objects.get(files='file')
        self.assertEqual(tender_instance.files, retrieve.files)
        retrieve.delete()
    
    def test_insert_online_payment(self):
        tender_instance = Tender.objects.create(tender_name='Tender1', tender_id='1234', winner='test1', files='file', online_payment='yes', url='test.com', end_date='2020-05-17', update_date='2020-05-14')
        tender_instance.save()
        retrieve = Tender.objects.get(online_payment='yes')
        self.assertEqual(tender_instance.online_payment, retrieve.online_payment)
        retrieve.delete()

    def test_insert_url(self):
        tender_instance = Tender.objects.create(tender_name='Tender1', tender_id='1234', winner='test1', files='file', online_payment='yes', url='test.com', end_date='2020-05-17', update_date='2020-05-14')
        tender_instance.save()
        retrieve = Tender.objects.get(url='test.com')
        self.assertEqual(tender_instance.url, retrieve.url)
        retrieve.delete()

    def test_insert_end_date(self):
        tender_instance = Tender.objects.create(tender_name='Tender1', tender_id='1234', winner='test1', files='file', online_payment='yes', url='test.com', end_date=datetime.date(2020,5,21), update_date=datetime.date(2020,5,19))
        tender_instance.save()
        retrieve = Tender.objects.get(end_date=datetime.date(2020,5,21), tender_name='Tender1')
        self.assertEqual(tender_instance.end_date, retrieve.end_date)
        retrieve.delete()

    def test_insert_update_date(self):
        tender_instance = Tender.objects.create(tender_name='Tender1', tender_id='1234', winner='test1', files='file', online_payment='yes', url='test.com', end_date=datetime.date(2020,5,26), update_date=datetime.date(2020,5,28))
        tender_instance.save()
        retrieve = Tender.objects.get(update_date=datetime.date(2020,5,28), tender_name='Tender1')
        self.assertEqual(tender_instance.update_date, retrieve.update_date)
        retrieve.delete()

if __name__ == '__main__':
    with open('test-reports/results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
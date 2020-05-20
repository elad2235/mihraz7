import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mihraz7.settings'
import unittest
import django
import xmlrunner
django.setup()

from django.test import Client
from tenders.models import Tender


class TestingTendersIntegration(unittest.TestCase):
    def test_add_delete_tender(self):
        tender_instance = Tender.objects.create(tender_name='Tender1', tender_id='1234', winner='test1', files='file', online_payment='yes', url='test.com', end_date='2020-05-17', update_date='2020-05-14')
        tender_instance.save()
        retrieve = Tender.objects.get(tender_name='Tender1')
        tender_instance.delete()
        self.assertNotEqual(None, retrieve.tender_id)
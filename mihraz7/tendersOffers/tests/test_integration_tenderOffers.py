import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mihraz7.settings'
import unittest
import django
django.setup()
from tendersOffers.models import TenderOffer
from tenders.models import Tender


class TestingTendersOffersIntegration(unittest.TestCase):

    def test_add_delete_tendersOffers(self):
        # Test add and delete functions
        tenderoffer_instance = TenderOffer.objects.create(id=1, tender_id='750', tender_name='test', first_name='sean', last_name='sean', email='test@test.com', offer='100')
        tenderoffer_instance.save()
        retrieve = TenderOffer.objects.get(tender_name='test')
        tenderoffer_instance.delete()
        self.assertNotEqual(None, retrieve.tender_id)
        Tender.objects.filter(tender_name='test').delete()

    def test_new_tender_submit_offer_cancel_offer(self):
        #Test tender functions -> submit offer -> cancel offer
        tender_instance = Tender.objects.create(tender_name='Tender1', tender_id='1234', winner='test1', files='file', online_payment='yes', url='test.com', end_date='2020-05-17', update_date='2020-05-14')
        tender_instance.save()
        retrieve_t = Tender.objects.get(tender_name='Tender1')
        self.assertEqual('Tender1', retrieve_t.tender_name)
        tenderoffer_instance = TenderOffer.objects.create(id=1, tender_id='1234', tender_name='Tender1', first_name='sean', last_name='sean', email='test@test.com', offer='100')
        tenderoffer_instance.save()
        retrieve_to = TenderOffer.objects.get(tender_name='Tender1')
        tenderoffer_instance.delete()
        self.assertNotEqual(None, retrieve_to.tender_id)
        tender_instance.delete()
        self.assertNotEqual(None, retrieve_t.tender_id)
        Tender.objects.filter(tender_name='Tender1').delete()

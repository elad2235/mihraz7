import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mihraz7.settings'
import unittest
import django
import xmlrunner
django.setup()

from tendersOffers.models import TenderOffer


class TestingTendersOffersIntegration(unittest.TestCase):
    def test_add_delete_tendersOffers(self):
        tenderoffer_instance = TenderOffer.objects.create(id=1, tender_id='750', tender_name='test', first_name='sean', last_name='sean', email='test@test.com', offer='100')
        tenderoffer_instance.save()
        retrieve = TenderOffer.objects.get(tender_name='test')
        tenderoffer_instance.delete()
        self.assertNotEqual(None, retrieve.tender_id)
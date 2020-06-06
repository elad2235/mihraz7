import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mihraz7.settings'
import unittest
import xmlrunner
from tendersOffers.models import TenderOffer
import django
django.setup()


class TestingTenderOffer(unittest.TestCase):

    def test_insert_id(self):
        tenderoffer_instance = TenderOffer.objects.create(id=1, tender_id='750', tender_name='test', first_name='sean', last_name='sean', email='test@test.com', offer='100')
        tenderoffer_instance.save()
        retrieve = TenderOffer.objects.get(id=1)
        self.assertEqual(tenderoffer_instance.id, retrieve.id)
        retrieve.delete()

    def test_insert_tender_id(self):
        tenderoffer_instance = TenderOffer.objects.create(id=1, tender_id='750', tender_name='test', first_name='sean', last_name='sean', email='test@test.com', offer='100')
        tenderoffer_instance.save()
        retrieve = TenderOffer.objects.get(tender_id='750')
        self.assertEqual(tenderoffer_instance.tender_id, retrieve.tender_id)
        retrieve.delete()

    def test_insert_tender_name(self):
        tenderoffer_instance = TenderOffer.objects.create(id=1, tender_id='750', tender_name='test', first_name='sean', last_name='sean', email='test@test.com', offer='100')
        tenderoffer_instance.save()
        retrieve = TenderOffer.objects.get(tender_name='test')
        self.assertEqual(tenderoffer_instance.tender_name, retrieve.tender_name)
        retrieve.delete()

    def test_insert_first_name(self):
        tenderoffer_instance = TenderOffer.objects.create(id=1, tender_id='750', tender_name='test', first_name='sean', last_name='sean1', email='test@test.com', offer='100')
        tenderoffer_instance.save()
        retrieve = TenderOffer.objects.get(first_name='sean')
        self.assertEqual(tenderoffer_instance.first_name, retrieve.first_name)
        retrieve.delete()

    def test_insert_last_name(self):
        tenderoffer_instance = TenderOffer.objects.create(id=1, tender_id='750', tender_name='test', first_name='sean', last_name='sean1', email='test@test.com', offer='100')
        tenderoffer_instance.save()
        retrieve = TenderOffer.objects.get(last_name='sean1')
        self.assertEqual(tenderoffer_instance.last_name, retrieve.last_name)
        retrieve.delete()

    def test_insert_offer(self):
        tenderoffer_instance = TenderOffer.objects.create(id=1, tender_id='750', tender_name='test', first_name='sean', last_name='sean', email='test@test.com', offer='100')
        tenderoffer_instance.save()
        retrieve = TenderOffer.objects.get(offer='100')
        self.assertEqual(tenderoffer_instance.offer, retrieve.offer)
        retrieve.delete()

    def test_insert_email(self):
        tenderoffer_instance = TenderOffer.objects.create(id=1, tender_id='750', tender_name='test', first_name='sean', last_name='sean', email='test@test.com', offer='100')
        tenderoffer_instance.save()
        retrieve = TenderOffer.objects.get(email='test@test.com')
        self.assertEqual(tenderoffer_instance.email, retrieve.email)
        retrieve.delete()

    def test_insert_tender(self):
        tenderoffer_instance = TenderOffer.objects.create(id=1, tender_id='750', tender_name='test', first_name='sean', last_name='sean', email='test@test.com', offer='100')
        tenderoffer_instance.save()
        retrieve = TenderOffer.objects.get(id=1)
        self.assertEqual(tenderoffer_instance.id, retrieve.id)
        retrieve.delete()

    def test_remove_tender(self):
        tenderoffer_instance = TenderOffer.objects.create(id=1, tender_id='750', tender_name='test', first_name='sean', last_name='sean', email='test@test.com', offer='100')
        tenderoffer_instance.save()
        tenderoffer_instance.delete()
        try:
            retrieve = TenderOffer.objects.get(id=1)

        except TenderOffer.DoesNotExist:
            retrieve = None
        self.assertEqual(None, retrieve)


if __name__ == '__main__':
    with open('test-reports/results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)

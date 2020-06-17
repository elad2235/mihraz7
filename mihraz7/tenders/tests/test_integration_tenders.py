import unittest
import os
from django.test import Client
from django.urls import reverse
from tenders.models import Comment
from tendersOffers.models import TenderOffer
os.environ['DJANGO_SETTINGS_MODULE'] = 'mihraz7.settings'
from tenders.models import Tender
import django
django.setup()


class TestingTendersIntegration(unittest.TestCase):
    def test_add_delete_tender(self):
        # test add and delete functions
        tender_instance = Tender.objects.create(tender_name='Tender111', tender_id='1234', winner='test1', files='file', online_payment='yes', url='test.com', end_date='2020-05-17', update_date='2020-05-14')
        tender_instance.save()
        retrieve = Tender.objects.get(tender_name='Tender111')
        tender_instance.delete()
        self.assertNotEqual(None, retrieve.tender_id)
        retrieve.delete()
        Tender.objects.filter(tender_name='Tender111').delete()

# Sprint 3 Revisioned:
    def test_connect_apply_disconnect(self):
        # Login -> apply for a tender form -> disconnect
        client = Client()
        #  Login Stage
        client.post('/login/', {'username': 'TestMe', 'password': '1342'}, follow=True)
        # Create Test Tender Stage
        tender_instance = Tender.objects.create(tender_name='_test_', tender_id='121212', winner='_test_', files='_test_', online_payment='_test_', url='test.com', end_date='2022-05-17', update_date='2022-05-14', Count_of_applied=0)
        tender_instance.save()
        retrieve = Tender.objects.get(tender_id='121212')
        self.assertEqual('_test_', retrieve.tender_name)
        # Apply Stage
        response = client.post('/tenders/RegisterOffer/?tenId=121212', {'Offer': '1337', 'tenId': '121212'}, follow=True)
        tender_offer = TenderOffer.objects.get(tender_id='121212', first_name='test', last_name='test')
        self.assertEqual(tender_offer.offer, '1337')
        # Disconnect Stage
        response = client.get('/account/logOut')
        self.assertEqual(response.status_code, 301)
        # cleanup
        tender_offer.delete()
        Tender.objects.filter(tender_name='_test_').delete()

    def test_connect_apply_cancel_disconnect(self):
        # login -> apply for a tender -> logout
        client = Client()
        # Login Stage
        client.post('/login/', {'username': 'TestMe', 'password': '1342'}, follow=True)
        # Create Test Tender Stage
        tender_instance = Tender.objects.create(tender_name='_test_', tender_id='131313', winner='_test_', files='_test_', online_payment='_test_', url='test.com', end_date='2022-05-17', update_date='2022-05-14', Count_of_applied=0)
        tender_instance.save()
        retrieve = Tender.objects.get(tender_id='131313')
        self.assertEqual('_test_', retrieve.tender_name)
        # Apply Stage
        response = client.post('/tenders/RegisterOffer/?t_lazyenId=131313', {'Offer': '1337', 'tenId': '131313'}, follow=True)
        tender_offer = TenderOffer.objects.get(tender_id='131313', first_name='test', last_name='test')
        self.assertEqual(tender_offer.offer, '1337')
        # Cancel Stage
        response = client.post('/tenders/RegisterOffer/?tenIdDelete=131313', {'tenIdDelete': '131313'}, follow=True)
        tender_offer = TenderOffer.objects.filter(tender_id='131313', first_name='test', last_name='test')
        self.assertEqual(tender_offer.count(), 0)
        # Disconnect Stage
        response = client.get('/account/logOut')
        self.assertEqual(response.status_code, 301)
        # cleanup
        tender_offer.delete()
        Tender.objects.filter(tender_name='_test_').delete()

    def test_connect_comment_disconnect(self):
        # Login -> comment on a tender -> disconnect
        client = Client()
        # Login Stage
        client.post('/login/', {'username': 'TestMe', 'password': '1342'}, follow=True)
        # Create Test Tender Stage
        tender_instance = Tender.objects.create(tender_name='_test_', tender_id='131313', winner='_test_', files='_test_', online_payment='_test_', url='test.com', end_date='2022-05-17', update_date='2022-05-14', Count_of_applied=0)
        tender_instance.save()
        retrieve = Tender.objects.get(tender_id='131313')
        self.assertEqual('_test_', retrieve.tender_name)
        # Post Comment On Tender Info Page Stage
        response = client.post(reverse('info_r', kwargs={'id': '131313'}, current_app='tenders'), {'comment_content': '_test_test'}, follow=False)
        self.assertEqual(response.status_code, 200)
        comment = Comment.objects.get(comment_content='_test_test')
        self.assertEqual(comment.comment_content, '_test_test')
        # Disconnect Stage
        response = client.get('/account/logOut')
        self.assertEqual(response.status_code, 301)
        # cleanup
        Tender.objects.filter(tender_name='_test_').delete()
        Comment.objects.filter(comment_content='_test_test').delete()

    def test_search_form_open_tender(self):
        # Login -> switch to open tenders -> use search form -> logout
        client = Client()
        # Login Stage
        client.post('/login/', {'username': 'TestMe', 'password': '1342'}, follow=True)
        # Create Test Tender Stage
        tender_instance = Tender.objects.create(tender_name='_test_', tender_id='131313', winner='_test_', files='_test_', online_payment='_test_', url='test.com', end_date='2022-05-17', update_date='2022-05-14', Count_of_applied=0)
        tender_instance.save()
        retrieve = Tender.objects.get(tender_id='131313')
        self.assertEqual('_test_', retrieve.tender_name)
        # Get Open Tender Page Stage
        response = client.get(reverse('Tender'))
        # Search Stage
        response = client.post('/tenders/Search/', {'search': '131313'}, follow=True)
        self.assertNotEqual(str(response.content).find('131313'), -1)
        # cleanup
        Tender.objects.filter(tender_name='_test_').delete()

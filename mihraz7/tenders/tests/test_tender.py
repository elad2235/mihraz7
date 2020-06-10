import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mihraz7.settings'
from tenders.models import Tender
from tenders.models import Comment
import unittest
import django
django.setup()
import xmlrunner
import datetime


class TestingTender(unittest.TestCase):

    def test_insert_tender_name(self):
        tender_instance = Tender.objects.create(tender_name='Tender1', tender_id='1234', winner='test1', files='file', online_payment='yes', url='test.com', end_date='2020-05-17', update_date='2020-05-14')
        tender_instance.save()
        retrieve = Tender.objects.get(tender_name='Tender1')
        self.assertEqual(tender_instance.tender_name, retrieve.tender_name)
        Tender.objects.filter(tender_name='Tender1').delete()

    def test_insert_tender_id(self):
        tender_instance = Tender.objects.create(tender_name='Tender1', tender_id='1234', winner='test1', files='file', online_payment='yes', url='test.com', end_date='2020-05-17', update_date='2020-05-14')
        tender_instance.save()
        retrieve = Tender.objects.get(tender_id='1234')
        self.assertEqual(tender_instance.tender_id, retrieve.tender_id)
        Tender.objects.filter(tender_name='Tender1').delete()

    def test_insert_winner(self):
        tender_instance = Tender.objects.create(tender_name='Tender1', tender_id='1234', winner='test1', files='file', online_payment='yes', url='test.com', end_date='2020-05-17', update_date='2020-05-14')
        tender_instance.save()
        retrieve = Tender.objects.get(winner='test1')
        self.assertEqual(tender_instance.winner, retrieve.winner)
        Tender.objects.filter(tender_name='Tender1').delete()

    def test_insert_files(self):
        tender_instance = Tender.objects.create(tender_name='Tender1', tender_id='1234', winner='test1', files='file', online_payment='yes', url='test.com', end_date='2020-05-17', update_date='2020-05-14')
        tender_instance.save()
        retrieve = Tender.objects.get(files='file')
        self.assertEqual(tender_instance.files, retrieve.files)
        Tender.objects.filter(tender_name='Tender1').delete()

    def test_insert_online_payment(self):
        tender_instance = Tender.objects.create(tender_name='Tender1', tender_id='1234', winner='test1', files='file', online_payment='yes', url='test.com', end_date='2020-05-17', update_date='2020-05-14')
        tender_instance.save()
        retrieve = Tender.objects.get(online_payment='yes')
        self.assertEqual(tender_instance.online_payment, retrieve.online_payment)
        Tender.objects.filter(tender_name='Tender1').delete()

    def test_insert_url(self):
        tender_instance = Tender.objects.create(tender_name='Tender1', tender_id='1234', winner='test1', files='file', online_payment='yes', url='test.com', end_date='2020-05-17', update_date='2020-05-14')
        tender_instance.save()
        retrieve = Tender.objects.get(url='test.com')
        self.assertEqual(tender_instance.url, retrieve.url)
        Tender.objects.filter(tender_name='Tender1').delete()

    def test_insert_end_date(self):
        tender_instance = Tender.objects.create(tender_name='Tender1', tender_id='1234', winner='test1', files='file', online_payment='yes', url='test.com', end_date=datetime.date(2020, 5, 21), update_date=datetime.date(2020, 5, 19))
        tender_instance.save()
        retrieve = Tender.objects.get(end_date=datetime.date(2020, 5, 21), tender_name='Tender1')
        self.assertEqual(tender_instance.end_date, retrieve.end_date)
        Tender.objects.filter(tender_name='Tender1').delete()

    def test_insert_update_date(self):
        tender_instance = Tender.objects.create(tender_name='Tender1', tender_id='1234', winner='test1', files='file', online_payment='yes', url='test.com', end_date=datetime.date(2020, 5, 26), update_date=datetime.date(2020, 5, 28))
        tender_instance.save()
        retrieve = Tender.objects.get(update_date=datetime.date(2020, 5, 28), tender_name='Tender1')
        self.assertEqual(tender_instance.update_date, retrieve.update_date)
        Tender.objects.filter(tender_name='Tender1').delete()

    def test_remove_tender(self):
        tender_instance = Tender.objects.create(tender_name='Tender1', tender_id='1234', winner='test1', files='file', online_payment='yes', url='test.com', end_date=datetime.date(2020, 5, 26), update_date=datetime.date(2020, 5, 28))
        tender_instance.save()
        tender_instance.delete()
        try:
            retrieve = Tender.objects.get(tender_name='Tender1')
        except Tender.DoesNotExist:
            retrieve = None
        self.assertEqual(None, retrieve)

    def test_insert_comment_name(self):
        comment_instance = Comment.objects.create(comment_name='Test1', comment_content='comment1', tender_id='1234')
        comment_instance.save()
        retrieve = Comment.objects.get(comment_name='Test1')
        self.assertEqual(comment_instance.comment_name, retrieve.comment_name)
        Comment.objects.filter(comment_name='Test1').delete()

    def test_insert_comment_content(self):
        comment_instance = Comment.objects.create(comment_name='Test1', comment_content='comment1', tender_id='1234')
        comment_instance.save()
        retrieve = Comment.objects.get(comment_content='comment1')
        self.assertEqual(comment_instance.comment_content, retrieve.comment_content)
        Comment.objects.filter(comment_content='comment1').delete()

    def test_insert_comment_id(self):
        comment_instance = Comment.objects.create(comment_name='Test1', comment_content='comment1', tender_id='1234')
        comment_instance.save()
        retrieve = Comment.objects.get(tender_id='1234')
        self.assertEqual(comment_instance.tender_id, retrieve.tender_id)
        Comment.objects.filter(tender_id='1234').delete()

    def test_remove_comment(self):
        comment_instance = Comment.objects.create(comment_name='Test1', comment_content='comment1', tender_id='1234')
        comment_instance.delete()
        try:
            retrieve = Comment.objects.get(comment_name='Test1')
        except Comment.DoesNotExist:
            retrieve = None
        self.assertEqual(None, retrieve)


if __name__ == '__main__':

    with open('test-reports/results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)

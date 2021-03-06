import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mihraz7.settings'
import unittest
import django
django.setup()
import xmlrunner
from suppliers.models import Supplier


class TestingSupplier(unittest.TestCase):

    def test_insert_supplier_name(self):
        supplier_instance = Supplier.objects.create(Supplier_name='Test1', Supplier_id='123', Service='testing')
        supplier_instance.save()
        retrieve = Supplier.objects.get(Supplier_name='Test1')
        self.assertEqual(supplier_instance.Supplier_name, retrieve.Supplier_name)
        retrieve.delete()

    def test_insert_Supplier_id(self):
        supplier_instance = Supplier.objects.create(Supplier_name='Test12', Supplier_id='1234', Service='testing1')
        supplier_instance.save()
        retrieve = Supplier.objects.get(Supplier_id='1234')
        self.assertEqual(supplier_instance.Supplier_id, retrieve.Supplier_id)
        retrieve.delete()

    def test_insert_Service(self):
        supplier_instance = Supplier.objects.create(Supplier_name='Test13', Supplier_id='1235', Service='testing2')
        supplier_instance.save()
        retrieve = Supplier.objects.get(Service='testing2')
        self.assertEqual(supplier_instance.Service, retrieve.Service)
        retrieve.delete()

    def test_insert_supplier(self):
        supplier_instance = Supplier.objects.create(Supplier_name='Test12', Supplier_id='1234', Service='testing1')
        supplier_instance.save()
        retrieve = Supplier.objects.get(Supplier_id='1234')
        self.assertEqual(supplier_instance.Supplier_id, retrieve.Supplier_id)
        retrieve.delete()

    def test_remove_supplier(self):
        supplier_instance = Supplier.objects.create(Supplier_name='Test12', Supplier_id='1234', Service='testing1')
        supplier_instance.save()
        supplier_instance.delete()
        try:
            retrieve = Supplier.objects.get(Supplier_id='1234')
        except Supplier.DoesNotExist:
            retrieve = None
        self.assertEqual(None, retrieve)


if __name__ == '__main__':
    with open('test-reports/results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)

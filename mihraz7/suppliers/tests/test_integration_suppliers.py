import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mihraz7.settings'
import unittest
import django
django.setup()
from suppliers.models import Supplier


class TestingSuppliersIntegration(unittest.TestCase):
    def test_add_delete_supplier(self):
        supplier_instance = Supplier.objects.create(Supplier_name='Test1', Supplier_id='123', Service='testing')
        supplier_instance.save()
        retrieve = Supplier.objects.get(Supplier_name='Test1')
        supplier_instance.delete()
        self.assertNotEqual(None, retrieve.Supplier_id)
    


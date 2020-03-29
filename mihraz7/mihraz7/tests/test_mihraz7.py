import unittest


class TestGeneralLogic(unittest.TestCase):
    def test_True(self):
        self.assertEqual(True,True)

    def test_False(self):
        self.assertEqual(False,False)

    def test_TrueFalse(self):
        self.assertNotEqual(True,False)

    
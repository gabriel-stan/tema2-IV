from django.test import TestCase


# Create your tests here.
class DummyTests(TestCase):
    def dummy_test(self):
        this_is_true = True
        self.assertEqual(this_is_true, False)
        print("dummy test passed")


class EmpresaTest(TestCase):
    def test(self):
        print "empresa test"


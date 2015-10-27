from django.test import TestCase
from votos.models import Empresa
from votos.models import Calificacion


# Create your tests here.
class DummyTests(TestCase):
    def test_dummy_test(self):
        this_is_true = True
        self.assertEqual(this_is_true, True)
        #print("dummy test passed")


class EmpresaTest(TestCase):
    def setUp(self):
        Empresa.objects.create(nombre = "TestEmpresa")
        Calificacion.objects.create(empresa = Empresa.objects.get(nombre = "TestEmpresa"), calificacion = 9)

    def test_all(self):
        emp = Empresa.objects.get(nombre = "TestEmpresa")
        cal = Calificacion.objects.get(empresa = emp)
        self.assertEqual(emp.nombre, "TestEmpresa")
        self.assertEqual(cal.empresa, emp)
        self.assertEqual(cal.calificacion, 9)
        self.assertEqual(emp.get_media(), 9.0)

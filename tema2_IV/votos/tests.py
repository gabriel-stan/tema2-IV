from django.test import TestCase
from votos.models import Empresa
from votos.models import Calificacion

from django.contrib.auth.models import User

from django.test import Client


# Create your tests here.
class DummyTests(TestCase):
    def test_dummy_test(self):
        this_is_true = True
        self.assertEqual(this_is_true, True)
        #print("dummy test passed")


class EmpresaTest(TestCase):
    def setUp(self):
        Empresa.objects.create(nombre = "TestEmpresa")
        usuario = User.objects.create_user(
            username='pepe', email='pepe@ugr.es', password='top_secret')
        Calificacion.objects.create(empresa = Empresa.objects.get(nombre = "TestEmpresa"), usuario=usuario, calificacion = 9)

    def test_all(self):
        emp = Empresa.objects.get(nombre = "TestEmpresa")
        cal = Calificacion.objects.get(empresa = emp)
        self.assertEqual(emp.nombre, "TestEmpresa")
        self.assertEqual(cal.empresa, emp)
        self.assertEqual(cal.calificacion, 9)
        self.assertEqual(emp.get_media(), 9.0)

class ViewsTest(TestCase):
    def setUp(self):

        # definimos cliente
        self.client = Client()

    def test_index(self):

        # respuesta de index
        response = self.client.get('/')
        # comprobamos codigo de retorno
        self.assertEqual(response.status_code, 200)

        count = Calificacion.objects.count()

        self.assertEqual(len(response.context['ultimas_calificaciones']), count)
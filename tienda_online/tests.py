from decimal import Decimal
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Categoria, Producto


class TiendaOnlineModelTests(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(
            nombre="Tecnología",
            descripcion="Artículos tecnológicos",
            activo=True
        )
        self.producto = Producto.objects.create(
            categoria=self.categoria,
            nombre="Audífonos Bluetooth",
            descripcion="Audífonos inalámbricos con cancelación de ruido",
            precio=Decimal("49990.00"),
            stock=20,
            disponible=True,
            habilitado=True
        )

    def test_categoria_creacion(self):
        self.assertEqual(str(self.categoria), "Tecnología")
        self.assertTrue(self.categoria.activo)

    def test_producto_creacion_y_habilitado(self):
        self.assertEqual(self.producto.nombre, "Audífonos Bluetooth")
        self.assertTrue(self.producto.habilitado)
        self.assertEqual(str(self.producto), "Audífonos Bluetooth ($49990.00)")


class TiendaOnlineViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.categoria = Categoria.objects.create(nombre="Periféricos", activo=True)
        self.producto = Producto.objects.create(
            categoria=self.categoria,
            nombre="Teclado Gamer",
            descripcion="Teclado mecánico",
            precio=29990.00,
            stock=15,
            habilitado=True
        )
        self.user = User.objects.create_user(username="testuser", password="password123")

    def test_vista_bienvenida(self):
        response = self.client.get(reverse('bienvenida'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tienda Online")

    def test_vista_listado_registros(self):
        response = self.client.get(reverse('listado_registros'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Teclado Gamer")

    def test_vista_detalle_registro(self):
        response = self.client.get(reverse('detalle_registro', kwargs={'pk': self.producto.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Teclado Gamer")

    def test_cambiar_estado_deshabilitar_habilitar(self):
        # Deshabilitar registro mediante POST
        response = self.client.post(
            reverse('cambiar_estado', kwargs={'pk': self.producto.pk}),
            {'habilitado': False}
        )
        self.assertEqual(response.status_code, 302)
        self.producto.refresh_from_db()
        self.assertFalse(self.producto.habilitado)

        # Habilitar registro nuevamente
        response = self.client.post(
            reverse('cambiar_estado', kwargs={'pk': self.producto.pk}),
            {'habilitado': True}
        )
        self.assertEqual(response.status_code, 302)
        self.producto.refresh_from_db()
        self.assertTrue(self.producto.habilitado)

    def test_crear_registro_vista(self):
        response = self.client.post(reverse('crear_registro'), {
            'categoria': self.categoria.pk,
            'nombre': 'Monitor 4K',
            'descripcion': 'Pantalla IPS 27 pulgadas',
            'precio': 249990.00,
            'stock': 8,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Producto.objects.filter(nombre='Monitor 4K').exists())

    def test_vista_login_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Iniciar Sesión")

    def test_vista_registro_get(self):
        response = self.client.get(reverse('registro'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Crear Cuenta")

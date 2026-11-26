from decimal import Decimal
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Categoria, Producto, Cliente, Pedido, DetallePedido
from .forms import CategoriaForm, ProductoForm, ClienteForm, PedidoForm


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
        self.cliente = Cliente.objects.create(
            nombre="Juan Pérez",
            email="juan.perez@example.com",
            telefono="+56912345678",
            direccion="Av. Providencia 1234",
            activo=True
        )
        self.pedido = Pedido.objects.create(
            cliente=self.cliente,
            estado='PENDIENTE',
            total=Decimal("49990.00")
        )
        self.detalle = DetallePedido.objects.create(
            pedido=self.pedido,
            producto=self.producto,
            cantidad=1,
            precio_unitario=Decimal("49990.00")
        )

    def test_categoria_creacion(self):
        self.assertEqual(str(self.categoria), "Tecnología")
        self.assertTrue(self.categoria.activo)

    def test_producto_creacion_y_habilitado(self):
        self.assertEqual(self.producto.nombre, "Audífonos Bluetooth")
        self.assertTrue(self.producto.habilitado)
        self.assertEqual(str(self.producto), "Audífonos Bluetooth ($49990.00)")

    def test_cliente_creacion(self):
        self.assertEqual(str(self.cliente), "Juan Pérez (juan.perez@example.com)")
        self.assertTrue(self.cliente.activo)

    def test_pedido_y_detalle_creacion(self):
        self.assertIn("Pedido #", str(self.pedido))
        self.assertEqual(self.pedido.detalles.count(), 1)
        self.assertEqual(self.pedido.detalles.first().producto, self.producto)


class TiendaOnlineFormsTests(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nombre="Computación")
        self.cliente = Cliente.objects.create(nombre="Ana Torres", email="ana@example.com")

    def test_categoria_form_valido(self):
        form = CategoriaForm(data={'nombre': 'Audio', 'descripcion': 'Sonido y audio', 'activo': True})
        self.assertTrue(form.is_valid())

    def test_producto_form_valido(self):
        form = ProductoForm(data={
            'categoria': self.categoria.id,
            'nombre': 'Mouse Óptico',
            'descripcion': 'Sensor 16000 DPI',
            'precio': '19990.00',
            'stock': 10,
            'disponible': True,
            'habilitado': True
        })
        self.assertTrue(form.is_valid())

    def test_cliente_form_valido(self):
        form = ClienteForm(data={
            'nombre': 'Carlos Silva',
            'email': 'carlos@example.com',
            'telefono': '+56987654321',
            'direccion': 'Calle Central 456',
            'activo': True
        })
        self.assertTrue(form.is_valid())

    def test_pedido_form_valido(self):
        form = PedidoForm(data={
            'cliente': self.cliente.id,
            'estado': 'PENDIENTE',
            'total': '35000.00'
        })
        self.assertTrue(form.is_valid())


class TiendaOnlineCBVTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.categoria = Categoria.objects.create(nombre="Periféricos", activo=True)
        self.producto = Producto.objects.create(
            categoria=self.categoria,
            nombre="Teclado Gamer",
            descripcion="Teclado mecánico RGB",
            precio=Decimal("29990.00"),
            stock=15,
            habilitado=True
        )
        self.cliente = Cliente.objects.create(
            nombre="María González",
            email="maria@example.com",
            telefono="+56999887766",
            direccion="Pasaje Los Alerces 789",
            activo=True
        )
        self.pedido = Pedido.objects.create(
            cliente=self.cliente,
            estado='PENDIENTE',
            total=Decimal("29990.00")
        )
        self.user = User.objects.create_user(username="testuser", password="password123")

    # --- Home & Auth ---
    def test_vista_bienvenida(self):
        response = self.client.get(reverse('bienvenida'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tienda Online")

    def test_vista_login_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Iniciar Sesión")

    def test_vista_registro_get(self):
        response = self.client.get(reverse('registro'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Crear Cuenta")

    # --- CBV: Producto ---
    def test_producto_list_view(self):
        response = self.client.get(reverse('producto_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Teclado Gamer")

    def test_producto_detail_view(self):
        response = self.client.get(reverse('producto_detail', kwargs={'pk': self.producto.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Teclado Gamer")

    def test_producto_create_view(self):
        response = self.client.post(reverse('producto_create'), {
            'categoria': self.categoria.pk,
            'nombre': 'Monitor 4K',
            'descripcion': 'Pantalla IPS 27 pulgadas',
            'precio': '249990.00',
            'stock': 8,
            'disponible': True,
            'habilitado': True,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Producto.objects.filter(nombre='Monitor 4K').exists())

    def test_producto_update_view(self):
        response = self.client.post(reverse('producto_update', kwargs={'pk': self.producto.pk}), {
            'categoria': self.categoria.pk,
            'nombre': 'Teclado Gamer Pro Editado',
            'descripcion': 'Nueva descripción',
            'precio': '34990.00',
            'stock': 12,
            'disponible': True,
            'habilitado': True,
        })
        self.assertEqual(response.status_code, 302)
        self.producto.refresh_from_db()
        self.assertEqual(self.producto.nombre, 'Teclado Gamer Pro Editado')

    def test_producto_delete_view(self):
        # GET confirm delete page
        response_get = self.client.get(reverse('producto_delete', kwargs={'pk': self.producto.pk}))
        self.assertEqual(response_get.status_code, 200)
        # POST delete
        response_post = self.client.post(reverse('producto_delete', kwargs={'pk': self.producto.pk}))
        self.assertEqual(response_post.status_code, 302)
        self.assertFalse(Producto.objects.filter(pk=self.producto.pk).exists())

    # --- CBV: Categoria ---
    def test_categoria_list_view(self):
        response = self.client.get(reverse('categoria_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Periféricos")

    def test_categoria_detail_view(self):
        response = self.client.get(reverse('categoria_detail', kwargs={'pk': self.categoria.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Periféricos")

    def test_categoria_create_view(self):
        response = self.client.post(reverse('categoria_create'), {
            'nombre': 'Almacenamiento',
            'descripcion': 'Discos SSD y HDD',
            'activo': True,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Categoria.objects.filter(nombre='Almacenamiento').exists())

    def test_categoria_update_view(self):
        response = self.client.post(reverse('categoria_update', kwargs={'pk': self.categoria.pk}), {
            'nombre': 'Periféricos y Accesorios',
            'descripcion': 'Descripción actualizada',
            'activo': True,
        })
        self.assertEqual(response.status_code, 302)
        self.categoria.refresh_from_db()
        self.assertEqual(self.categoria.nombre, 'Periféricos y Accesorios')

    def test_categoria_delete_view(self):
        nueva_cat = Categoria.objects.create(nombre="Para Borrar")
        response_get = self.client.get(reverse('categoria_delete', kwargs={'pk': nueva_cat.pk}))
        self.assertEqual(response_get.status_code, 200)
        response_post = self.client.post(reverse('categoria_delete', kwargs={'pk': nueva_cat.pk}))
        self.assertEqual(response_post.status_code, 302)
        self.assertFalse(Categoria.objects.filter(pk=nueva_cat.pk).exists())

    # --- CBV: Cliente ---
    def test_cliente_list_view(self):
        response = self.client.get(reverse('cliente_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "María González")

    def test_cliente_detail_view(self):
        response = self.client.get(reverse('cliente_detail', kwargs={'pk': self.cliente.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "María González")

    def test_cliente_create_view(self):
        response = self.client.post(reverse('cliente_create'), {
            'nombre': 'Pedro Morales',
            'email': 'pedro@example.com',
            'telefono': '+56911223344',
            'direccion': 'Calle Norte 123',
            'activo': True,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Cliente.objects.filter(email='pedro@example.com').exists())

    def test_cliente_update_view(self):
        response = self.client.post(reverse('cliente_update', kwargs={'pk': self.cliente.pk}), {
            'nombre': 'María González Editada',
            'email': 'maria_nueva@example.com',
            'telefono': '+56999887700',
            'direccion': 'Nueva Dirección 123',
            'activo': True,
        })
        self.assertEqual(response.status_code, 302)
        self.cliente.refresh_from_db()
        self.assertEqual(self.cliente.nombre, 'María González Editada')

    def test_cliente_delete_view(self):
        nuevo_cli = Cliente.objects.create(nombre="Temporal", email="temp@example.com")
        response_get = self.client.get(reverse('cliente_delete', kwargs={'pk': nuevo_cli.pk}))
        self.assertEqual(response_get.status_code, 200)
        response_post = self.client.post(reverse('cliente_delete', kwargs={'pk': nuevo_cli.pk}))
        self.assertEqual(response_post.status_code, 302)
        self.assertFalse(Cliente.objects.filter(pk=nuevo_cli.pk).exists())

    # --- CBV: Pedido ---
    def test_pedido_list_view(self):
        response = self.client.get(reverse('pedido_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, str(self.pedido.id))

    def test_pedido_detail_view(self):
        response = self.client.get(reverse('pedido_detail', kwargs={'pk': self.pedido.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, str(self.pedido.id))

    def test_pedido_create_view(self):
        response = self.client.post(reverse('pedido_create'), {
            'cliente': self.cliente.pk,
            'estado': 'PAGADO',
            'total': '89990.00',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Pedido.objects.filter(total=Decimal('89990.00')).exists())

    def test_pedido_update_view(self):
        response = self.client.post(reverse('pedido_update', kwargs={'pk': self.pedido.pk}), {
            'cliente': self.cliente.pk,
            'estado': 'ENVIADO',
            'total': '29990.00',
        })
        self.assertEqual(response.status_code, 302)
        self.pedido.refresh_from_db()
        self.assertEqual(self.pedido.estado, 'ENVIADO')

    def test_pedido_delete_view(self):
        nuevo_ped = Pedido.objects.create(cliente=self.cliente, estado='PENDIENTE', total=100)
        response_get = self.client.get(reverse('pedido_delete', kwargs={'pk': nuevo_ped.pk}))
        self.assertEqual(response_get.status_code, 200)
        response_post = self.client.post(reverse('pedido_delete', kwargs={'pk': nuevo_ped.pk}))
        self.assertEqual(response_post.status_code, 302)
        self.assertFalse(Pedido.objects.filter(pk=nuevo_ped.pk).exists())

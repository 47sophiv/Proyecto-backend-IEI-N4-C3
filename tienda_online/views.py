from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication

from .models import Categoria, Producto, Cliente, Pedido, DetallePedido
from .forms import ProductoForm, CambiarEstadoForm
from .serializer import (
    CategoriaSerializer,
    ProductoSerializer,
    ClienteSerializer,
    PedidoSerializer,
    DetallePedidoSerializer,
)


# ==============================================================================
# 1. Página de Inicio y Vistas Principales (Sección 7)
# ==============================================================================

def bienvenida(request):
    """
    Vista principal de la aplicación Tienda Online.
    Demuestra el manejo de variables, estructuras de control, contexto dinámico
    y el uso de sesiones con request.session (Sección 21).
    """
    # Almacenar mensaje en la sesión según Sección 21 de la guía
    request.session['mensaje_bienvenida'] = '¡Bienvenido a Tienda Online!'

    titulo_proyecto = 'Tienda Online'
    subtitulo = 'API & Comercio Electrónico'
    numero_proyecto = 8
    servidor_activo = True
    descripcion_sistema = (
        'Sistema digital para la gestión de ventas, pedidos e inventario de comercio electrónico. '
        'Selecciona un módulo para comenzar.'
    )

    modulos = [
        {
            'id': 1,
            'nombre': 'Catálogo de Productos',
            'icono': '📦',
            'descripcion': 'Administra el inventario, categorías, stock y precios de la tienda.',
            'url': '/registros/',
            'color': 'blue',
            'color_clase': 'bg-blue-600',
            'hover_clase': 'hover:bg-blue-700',
            'borde_clase': 'border-blue-100',
            'activo': True,
        },
        {
            'id': 2,
            'nombre': 'Ventas y Pedidos',
            'icono': '🛒',
            'descripcion': 'Control de compras, seguimiento de estados y órdenes de clientes.',
            'url': '/api/pedidos/',
            'color': 'emerald',
            'color_clase': 'bg-emerald-600',
            'hover_clase': 'hover:bg-emerald-700',
            'borde_clase': 'border-emerald-100',
            'activo': True,
        },
        {
            'id': 3,
            'nombre': 'Clientes & Usuarios',
            'icono': '👥',
            'descripcion': 'Registro de usuarios, perfiles de compradores y operadores.',
            'url': '/api/clientes/',
            'color': 'purple',
            'color_clase': 'bg-purple-600',
            'hover_clase': 'hover:bg-purple-700',
            'borde_clase': 'border-purple-100',
            'activo': True,
        },
        {
            'id': 4,
            'nombre': 'Métricas & Reportes',
            'icono': '📊',
            'descripcion': 'Indicadores de gestión, tendencias de ventas y estadísticas.',
            'url': '/api/',
            'color': 'amber',
            'color_clase': 'bg-amber-500',
            'hover_clase': 'hover:bg-amber-600',
            'borde_clase': 'border-amber-100',
            'activo': True,
        },
    ]

    contexto = {
        'titulo': titulo_proyecto,
        'subtitulo': subtitulo,
        'numero_proyecto': numero_proyecto,
        'servidor_activo': servidor_activo,
        'descripcion': descripcion_sistema,
        'modulos': modulos,
        'total_modulos': len(modulos),
        'mensaje_sesion': request.session.get('mensaje_bienvenida', ''),
    }

    return render(request, 'tienda_online/bienvenida.html', contexto)


# ==============================================================================
# 2. Control de Errores 404 (Sección 8)
# ==============================================================================

def error_404(request, exception=None, *args, **kwargs):
    """
    Vista personalizada para manejar errores HTTP 404.
    """
    contexto = {
        'titulo_error': 'Error 404',
        'mensaje_error': 'Página o función no disponible en Tienda Online',
        'descripcion_error': 'Esta función de la Tienda Online aún está en etapa de desarrollo o la ruta no existe.',
    }
    return render(request, '404.html', contexto, status=404)


# ==============================================================================
# 3. CRUD Manual con Vistas Basadas en Clases (CBV) (Sección 20)
# ==============================================================================

class RegistroListView(ListView):
    """
    ListView para listar registros del modelo Producto en la plantilla lista_registros.html.
    """
    model = Producto
    template_name = 'tienda_online/registros/lista_registros.html'
    context_object_name = 'object_list'
    ordering = ['-id']


class RegistroCreateView(CreateView):
    """
    CreateView para procesar la creación de un nuevo Producto con ProductoForm.
    """
    model = Producto
    form_class = ProductoForm
    template_name = 'tienda_online/registros/crear_registro.html'
    success_url = reverse_lazy('listado_registros')

    def form_valid(self, form):
        messages.success(self.request, "Registro creado exitosamente.")
        return super().form_valid(form)


class RegistroUpdateView(UpdateView):
    """
    UpdateView para editar los datos de un Producto existente mediante su pk.
    """
    model = Producto
    form_class = ProductoForm
    template_name = 'tienda_online/registros/editar_registro.html'
    success_url = reverse_lazy('listado_registros')

    def form_valid(self, form):
        messages.success(self.request, "Registro actualizado correctamente.")
        return super().form_valid(form)


class CambiarEstadoView(UpdateView):
    """
    UpdateView especializada para habilitar o deshabilitar un registro
    (eliminado lógico) sin borrarlo de la base de datos.
    """
    model = Producto
    form_class = CambiarEstadoForm

    def form_valid(self, form):
        self.object = form.save()
        return redirect('listado_registros')


class RegistroDetailView(DetailView):
    """
    DetailView para consultar la información detallada de un Producto.
    """
    model = Producto
    template_name = 'tienda_online/registros/detalle_registro.html'
    context_object_name = 'registro'


# Aliases para compatibilidad con nomenclaturas de Producto
ProductoListView = RegistroListView
ProductoCreateView = RegistroCreateView
ProductoUpdateView = RegistroUpdateView
ProductoDetailView = RegistroDetailView


# ==============================================================================
# 4. Autenticación y Gestión de Sesiones (Sección 21)
# ==============================================================================

def registro(request):
    """
    Vista FBV para el registro de nuevos usuarios mediante UserCreationForm.
    Inicia sesión automáticamente tras un registro exitoso.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro Exitoso. ¡Bienvenido a Tienda Online!")
            return redirect('/')
        else:
            messages.error(request, "No ha sido posible registrarlo. Por favor revise el formulario por errores.")
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})


def logout_view(request):
    """
    Cierra la sesión del usuario y redirige al login.
    """
    logout(request)
    return redirect('login')


@login_required
def vista_protegida(request):
    """
    Vista de demostración protegida con @login_required y uso de request.session.
    """
    request.session['ultimo_acceso'] = 'Reciente'
    return render(request, 'tienda_online/vista_protegida.html', {
        'mensaje': 'Acceso autorizado al área protegida.',
        'usuario': request.user
    })


# ==============================================================================
# 5. Vistas Basadas en Clases (CBV) para DRF (Secciones 14-17)
# ==============================================================================

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [SessionAuthentication]


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    authentication_classes = [SessionAuthentication]


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [SessionAuthentication]


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    authentication_classes = [SessionAuthentication]


class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
    authentication_classes = [SessionAuthentication]

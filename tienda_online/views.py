from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication

from .models import Categoria, Producto, Cliente, Pedido, DetallePedido
from .forms import (
    ProductoForm,
    CategoriaForm,
    ClienteForm,
    PedidoForm,
    CambiarEstadoForm,
    RegistroUsuarioForm,
)
from .serializer import (
    CategoriaSerializer,
    ProductoSerializer,
    ClienteSerializer,
    PedidoSerializer,
    DetallePedidoSerializer,
)


# ==============================================================================
# 1. Página de Inicio y Vistas Principales (Vista pública obligatoria)
# ==============================================================================

def bienvenida(request):
    """
    Vista pública principal de la aplicación Tienda Online.
    Presenta la interfaz de navegación, catálogo de módulos y acceso a los CRUDs.
    """
    request.session['mensaje_bienvenida'] = '¡Bienvenido a Tienda Online!'

    titulo_proyecto = 'Tienda Online'
    subtitulo = 'API & Comercio Electrónico'
    numero_proyecto = 8
    servidor_activo = True
    descripcion_sistema = (
        'Sistema digital para la gestión de productos, categorías, clientes y pedidos. '
        'Selecciona una entidad para gestionar su CRUD completo mediante Vistas Basadas en Clases (CBV).'
    )

    modulos = [
        {
            'id': 1,
            'nombre': 'Catálogo de Productos',
            'icono': '📦',
            'descripcion': 'CRUD completo de inventario, precios, stock y eliminación.',
            'url': '/productos/',
            'color': 'blue',
            'color_clase': 'bg-blue-600',
            'hover_clase': 'hover:bg-blue-700',
            'borde_clase': 'border-blue-100',
            'activo': True,
        },
        {
            'id': 2,
            'nombre': 'Categorías',
            'icono': '🏷️',
            'descripcion': 'Gestión y clasificación de familias de productos.',
            'url': '/categorias/',
            'color': 'indigo',
            'color_clase': 'bg-indigo-600',
            'hover_clase': 'hover:bg-indigo-700',
            'borde_clase': 'border-indigo-100',
            'activo': True,
        },
        {
            'id': 3,
            'nombre': 'Clientes',
            'icono': '👥',
            'descripcion': 'Administración de clientes, correos y direcciones.',
            'url': '/clientes/',
            'color': 'purple',
            'color_clase': 'bg-purple-600',
            'hover_clase': 'hover:bg-purple-700',
            'borde_clase': 'border-purple-100',
            'activo': True,
        },
        {
            'id': 4,
            'nombre': 'Ventas y Pedidos',
            'icono': '🛒',
            'descripcion': 'Seguimiento de pedidos, estados de entrega y montos totales.',
            'url': '/pedidos/',
            'color': 'emerald',
            'color_clase': 'bg-emerald-600',
            'hover_clase': 'hover:bg-emerald-700',
            'borde_clase': 'border-emerald-100',
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
        'total_productos': Producto.objects.count(),
        'total_categorias': Categoria.objects.count(),
        'total_clientes': Cliente.objects.count(),
        'total_pedidos': Pedido.objects.count(),
        'mensaje_sesion': request.session.get('mensaje_bienvenida', ''),
    }

    return render(request, 'tienda_online/bienvenida.html', contexto)


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
# 2. CRUD CBV: Entidad PRODUCTO (Evaluación 3 - Criterio 2)
# ==============================================================================

class ProductoListView(ListView):
    model = Producto
    template_name = 'tienda_online/productos/producto_list.html'
    context_object_name = 'object_list'
    ordering = ['-id']


class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'tienda_online/productos/producto_detail.html'
    context_object_name = 'producto'


class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'tienda_online/productos/producto_form.html'
    success_url = reverse_lazy('producto_list')

    def form_valid(self, form):
        messages.success(self.request, "Producto creado exitosamente.")
        return super().form_valid(form)


class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'tienda_online/productos/producto_form.html'
    success_url = reverse_lazy('producto_list')

    def form_valid(self, form):
        messages.success(self.request, "Producto actualizado correctamente.")
        return super().form_valid(form)


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'tienda_online/productos/producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')
    context_object_name = 'producto'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Producto eliminado correctamente.")
        return super().delete(request, *args, **kwargs)


class CambiarEstadoView(UpdateView):
    """
    Acción rápida para cambiar el estado habilitado de un producto vía AJAX / POST.
    """
    model = Producto
    form_class = CambiarEstadoForm

    def form_valid(self, form):
        self.object = form.save()
        return redirect('producto_list')


# Aliases para compatibilidad con evaluaciones previas
RegistroListView = ProductoListView
RegistroCreateView = ProductoCreateView
RegistroUpdateView = ProductoUpdateView
RegistroDetailView = ProductoDetailView
RegistroDeleteView = ProductoDeleteView


# ==============================================================================
# 3. CRUD CBV: Entidad CATEGORIA (Evaluación 3 - Criterio 2)
# ==============================================================================

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'tienda_online/categorias/categoria_list.html'
    context_object_name = 'categorias'
    ordering = ['nombre']


class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'tienda_online/categorias/categoria_detail.html'
    context_object_name = 'categoria'


class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'tienda_online/categorias/categoria_form.html'
    success_url = reverse_lazy('categoria_list')

    def form_valid(self, form):
        messages.success(self.request, "Categoría creada exitosamente.")
        return super().form_valid(form)


class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'tienda_online/categorias/categoria_form.html'
    success_url = reverse_lazy('categoria_list')

    def form_valid(self, form):
        messages.success(self.request, "Categoría actualizada correctamente.")
        return super().form_valid(form)


class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'tienda_online/categorias/categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria_list')
    context_object_name = 'categoria'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Categoría eliminada correctamente.")
        return super().delete(request, *args, **kwargs)


# ==============================================================================
# 4. CRUD CBV: Entidad CLIENTE (Evaluación 3 - Criterio 2)
# ==============================================================================

class ClienteListView(ListView):
    model = Cliente
    template_name = 'tienda_online/clientes/cliente_list.html'
    context_object_name = 'clientes'
    ordering = ['-id']


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'tienda_online/clientes/cliente_detail.html'
    context_object_name = 'cliente'


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'tienda_online/clientes/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

    def form_valid(self, form):
        messages.success(self.request, "Cliente registrado exitosamente.")
        return super().form_valid(form)


class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'tienda_online/clientes/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

    def form_valid(self, form):
        messages.success(self.request, "Datos del cliente actualizados correctamente.")
        return super().form_valid(form)


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'tienda_online/clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')
    context_object_name = 'cliente'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Cliente eliminado correctamente.")
        return super().delete(request, *args, **kwargs)


# ==============================================================================
# 5. CRUD CBV: Entidad PEDIDO (Evaluación 3 - Criterio 2)
# ==============================================================================

class PedidoListView(ListView):
    model = Pedido
    template_name = 'tienda_online/pedidos/pedido_list.html'
    context_object_name = 'pedidos'
    ordering = ['-fecha_pedido']


class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'tienda_online/pedidos/pedido_detail.html'
    context_object_name = 'pedido'


class PedidoCreateView(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'tienda_online/pedidos/pedido_form.html'
    success_url = reverse_lazy('pedido_list')

    def form_valid(self, form):
        messages.success(self.request, "Pedido registrado exitosamente.")
        return super().form_valid(form)


class PedidoUpdateView(UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'tienda_online/pedidos/pedido_form.html'
    success_url = reverse_lazy('pedido_list')

    def form_valid(self, form):
        messages.success(self.request, "Pedido actualizado correctamente.")
        return super().form_valid(form)


class PedidoDeleteView(DeleteView):
    model = Pedido
    template_name = 'tienda_online/pedidos/pedido_confirm_delete.html'
    success_url = reverse_lazy('pedido_list')
    context_object_name = 'pedido'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Pedido eliminado correctamente.")
        return super().delete(request, *args, **kwargs)


# ==============================================================================
# 6. Autenticación y Gestión de Sesiones
# ==============================================================================

def registro(request):
    """
    Vista FBV para el registro de nuevos usuarios mediante RegistroUsuarioForm.
    Inicia sesión automáticamente tras un registro exitoso.
    """
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro Exitoso. ¡Bienvenido a Tienda Online!")
            return redirect('/')
        else:
            messages.error(request, "No ha sido posible registrarlo. Por favor revise el formulario por errores.")
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registration/registro.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def vista_protegida(request):
    request.session['ultimo_acceso'] = 'Reciente'
    return render(request, 'tienda_online/vista_protegida.html', {
        'mensaje': 'Acceso autorizado al área protegida.',
        'usuario': request.user
    })


# ==============================================================================
# 7. Vistas Basadas en Clases (CBV) para DRF (API REST Acumulativa)
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

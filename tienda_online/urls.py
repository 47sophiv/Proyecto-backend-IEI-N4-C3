from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Router para las Vistas Basadas en Clases (CBV) / ViewSets de DRF
router = DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'clientes', views.ClienteViewSet)
router.register(r'pedidos', views.PedidoViewSet)
router.register(r'detalles-pedidos', views.DetallePedidoViewSet)

urlpatterns = [
    # 1. Página principal de bienvenida (Vista pública obligatoria)
    path('', views.bienvenida, name='bienvenida'),

    # CRUD mediante vistas basadas en funciones (FBV)
    path('fbv/categorias/', views.categoria_fbv_list, name='categoria_fbv_list'),
    path('fbv/categorias/crear/', views.categoria_fbv_create, name='categoria_fbv_create'),
    path('fbv/categorias/<int:pk>/', views.categoria_fbv_detail, name='categoria_fbv_detail'),
    path('fbv/categorias/<int:pk>/editar/', views.categoria_fbv_update, name='categoria_fbv_update'),
    path('fbv/categorias/<int:pk>/eliminar/', views.categoria_fbv_delete, name='categoria_fbv_delete'),

    # 2. CRUD CBV: PRODUCTOS (ListView, DetailView, CreateView, UpdateView, DeleteView)
    path('productos/', views.ProductoListView.as_view(), name='producto_list'),
    path('productos/crear/', views.ProductoCreateView.as_view(), name='producto_create'),
    path('productos/<int:pk>/', views.ProductoDetailView.as_view(), name='producto_detail'),
    path('productos/<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='producto_update'),
    path('productos/<int:pk>/eliminar/', views.ProductoDeleteView.as_view(), name='producto_delete'),
    path('productos/<int:pk>/cambiar_estado/', views.CambiarEstadoView.as_view(), name='producto_cambiar_estado'),

    # Rutas alias para compatibilidad con evaluaciones previas
    path('registros/', views.RegistroListView.as_view(), name='listado_registros'),
    path('registros/crear/', views.RegistroCreateView.as_view(), name='crear_registro'),
    path('registros/<int:pk>/', views.RegistroDetailView.as_view(), name='detalle_registro'),
    path('registros/<int:pk>/detalle/', views.RegistroDetailView.as_view(), name='detalle_registro_alias'),
    path('registros/<int:pk>/editar/', views.RegistroUpdateView.as_view(), name='editar_registro'),
    path('registros/<int:pk>/eliminar/', views.RegistroDeleteView.as_view(), name='eliminar_registro'),
    path('registros/<int:pk>/cambiar_estado/', views.CambiarEstadoView.as_view(), name='cambiar_estado'),

    # 3. CRUD CBV: CATEGORIAS (ListView, DetailView, CreateView, UpdateView, DeleteView)
    path('categorias/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/crear/', views.CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria_detail'),
    path('categorias/<int:pk>/editar/', views.CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/eliminar/', views.CategoriaDeleteView.as_view(), name='categoria_delete'),

    # 4. CRUD CBV: CLIENTES (ListView, DetailView, CreateView, UpdateView, DeleteView)
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('clientes/crear/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/<int:pk>/eliminar/', views.ClienteDeleteView.as_view(), name='cliente_delete'),

    # 5. CRUD CBV: PEDIDOS (ListView, DetailView, CreateView, UpdateView, DeleteView)
    path('pedidos/', views.PedidoListView.as_view(), name='pedido_list'),
    path('pedidos/crear/', views.PedidoCreateView.as_view(), name='pedido_create'),
    path('pedidos/<int:pk>/', views.PedidoDetailView.as_view(), name='pedido_detail'),
    path('pedidos/<int:pk>/editar/', views.PedidoUpdateView.as_view(), name='pedido_update'),
    path('pedidos/<int:pk>/eliminar/', views.PedidoDeleteView.as_view(), name='pedido_delete'),

    # 6. Vista de sesión protegida
    path('protegida/', views.vista_protegida, name='vista_protegida'),

    # 7. Rutas API REST generadas por el router de DRF (Requerimiento acumulativo)
    path('api/', include(router.urls)),

    # 8. Ruta directa para verificar la plantilla 404
    path('404/', views.error_404, name='error_404'),
]

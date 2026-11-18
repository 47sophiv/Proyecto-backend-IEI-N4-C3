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
    # 1. Página principal de bienvenida
    path('', views.bienvenida, name='bienvenida'),

    # 2. Rutas CRUD manual tradicional (Sección 20 de la guía)
    path('registros/', views.RegistroListView.as_view(), name='listado_registros'),
    path('registros/crear/', views.RegistroCreateView.as_view(), name='crear_registro'),
    path('registros/<int:pk>/editar/', views.RegistroUpdateView.as_view(), name='editar_registro'),
    path('registros/<int:pk>/detalle/', views.RegistroDetailView.as_view(), name='detalle_registro'),
    path('registros/<int:pk>/cambiar_estado/', views.CambiarEstadoView.as_view(), name='cambiar_estado'),

    # Rutas aliadas para productos
    path('productos/', views.ProductoListView.as_view(), name='productos_listado'),
    path('productos/crear/', views.ProductoCreateView.as_view(), name='productos_crear'),
    path('productos/<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='productos_editar'),
    path('productos/<int:pk>/detalle/', views.ProductoDetailView.as_view(), name='productos_detalle'),

    # 3. Vista de sesión protegida (Sección 21 de la guía)
    path('protegida/', views.vista_protegida, name='vista_protegida'),

    # 4. Rutas API REST generadas por el router de DRF (Secciones 18 y 19)
    path('api/', include(router.urls)),

    # 5. Ruta directa para verificar la plantilla 404 (Sección 8)
    path('404/', views.error_404, name='error_404'),
]

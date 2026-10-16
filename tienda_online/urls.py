from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from . import views

# Espacio de nombres de la aplicacion
app_name = 'tienda_online'

# Router para las Vistas Basadas en Clases (CBV) / ViewSets
router = DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'clientes', views.ClienteViewSet)
router.register(r'pedidos', views.PedidoViewSet)
router.register(r'detalles-pedidos', views.DetallePedidoViewSet)

urlpatterns = [
    # Ruta principal: Pagina de bienvenida de la Tienda Online
    path('', views.bienvenida, name='bienvenida'),
    # Rutas API REST generadas por el router de DRF
    path('api/', include(router.urls)),
    # Ruta directa para verificar la plantilla 404
    path('404/', views.error_404, name='error_404'),
    # Ruta comodin (catch-all): captura rutas no encontradas excluyendo archivos estáticos
    re_path(r'^(?!static/).*$', views.error_404, name='catch_all_404'),
]


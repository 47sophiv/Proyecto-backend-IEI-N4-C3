from django.urls import path
from . import views

# Espacio de nombres de la aplicacion
app_name = 'tienda_online'

urlpatterns = [
    # Ruta principal: Pagina de bienvenida de la Tienda Online
    path('', views.bienvenida, name='bienvenida'),
    # Ruta directa para verificar la plantilla 404
    path('404/', views.error_404, name='error_404'),
]

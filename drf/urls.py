"""
Configuración global de URLs para el proyecto drf.
Incluye rutas administrativas, autenticación nativa de Django y la aplicación tienda_online.
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from tienda_online import views as tienda_views

urlpatterns = [
    # Panel de administración de Django (Sección 15 y 22)
    path('admin/', admin.site.urls),

    # URLs de autenticación listas para usar (Sección 21 de la guía)
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('registro/', tienda_views.registro, name='registro'),

    # Delegación de rutas hacia la aplicación tienda_online (Sección 19)
    path('mi_aplicacion/', include('tienda_online.urls')),
    path('', include('tienda_online.urls')),
]

urlpatterns += staticfiles_urlpatterns()

# Manejador global para el error 404 personalizado (Sección 8)
handler404 = 'tienda_online.views.error_404'

from django.shortcuts import render

def bienvenida(request):
    """
    Vista principal de la aplicación Tienda Online.
    Demuestra el manejo de variables, tipos de datos (str, int, bool, list, dict)
    y el paso de contexto dinámico a la plantilla HTML.
    """
    # Variables de configuración y presentación (Criterio 1: Variables y tipos de datos)
    titulo_proyecto = 'Tienda Online'
    subtitulo = 'API & Comercio Electrónico'
    numero_proyecto = 8
    servidor_activo = True
    descripcion_sistema = (
        'Sistema digital para la gestión de ventas, pedidos e inventario de comercio electrónico. '
        'Selecciona un módulo para comenzar.'
    )

    # Estructura compleja: Lista de diccionarios que modelan los módulos del negocio
    modulos = [
        {
            'id': 1,
            'nombre': 'Catálogo de Productos',
            'icono': '📦',
            'descripcion': 'Administra el inventario, categorías, stock y precios de la tienda.',
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
            'color': 'amber',
            'color_clase': 'bg-amber-500',
            'hover_clase': 'hover:bg-amber-600',
            'borde_clase': 'border-amber-100',
            'activo': True,
        },
    ]

    # Operaciones: cálculo de total de módulos disponibles
    total_modulos = len(modulos)

    # Diccionario de contexto para inyectar en la plantilla
    contexto = {
        'titulo': titulo_proyecto,
        'subtitulo': subtitulo,
        'numero_proyecto': numero_proyecto,
        'servidor_activo': servidor_activo,
        'descripcion': descripcion_sistema,
        'modulos': modulos,
        'total_modulos': total_modulos,
    }

    return render(request, 'tienda_online/bienvenida.html', contexto)


def error_404(request, exception=None):
    """
    Vista personalizada para manejar errores HTTP 404 (Página no encontrada).
    Captura la excepción y retorna la plantilla 404.html con código de estado 404.
    """
    contexto = {
        'titulo_error': 'Error 404',
        'mensaje_error': 'Página o función no disponible en Tienda Online',
        'descripcion_error': 'Esta función de la Tienda Online aún está en etapa de desarrollo o la ruta no existe.',
    }
    return render(request, '404.html', contexto, status=404)


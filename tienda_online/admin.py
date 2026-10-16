from django.contrib import admin
from .models import Categoria, Producto, Cliente, Pedido, DetallePedido


class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 1


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'activo', 'created_at')
    list_filter = ('activo',)
    search_fields = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'precio', 'stock', 'disponible', 'created_at')
    list_filter = ('categoria', 'disponible')
    search_fields = ('nombre', 'descripcion')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'telefono', 'activo', 'created_at')
    list_filter = ('activo',)
    search_fields = ('nombre', 'email')


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'estado', 'total', 'fecha_pedido')
    list_filter = ('estado', 'fecha_pedido')
    search_fields = ('cliente__nombre', 'cliente__email')
    inlines = [DetallePedidoInline]


@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'pedido', 'producto', 'cantidad', 'precio_unitario')
    list_filter = ('pedido',)
    search_fields = ('producto__nombre', 'pedido__id')


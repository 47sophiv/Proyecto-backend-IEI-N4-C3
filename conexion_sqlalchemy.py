"""
Script de demostración y prueba de conexión usando el ORM SQLAlchemy con MySQL.
Permite interactuar con la base de datos 'mi_tienda' mediante consultas y mapeo relacional.
"""
from sqlalchemy import create_engine, text

# Cadena de conexión con el usuario configurado: mysql://usuario:contraseña@servidor:puerto/base_de_datos
DATABASE_URL = "mysql://mi_tienda:Tienda1@127.0.0.1:3306/mi_tienda"


def probar_conexion():
    print("Conectando a MySQL mediante SQLAlchemy...")
    engine = create_engine(DATABASE_URL)

    with engine.connect() as conexion:
        # Verificar versión del motor
        version = conexion.execute(text("SELECT VERSION()")).scalar()
        print(f" Conexión exitosa. Versión de MySQL: {version}")

        # Consultar categorías cargadas
        categorias = conexion.execute(text("SELECT id, nombre, activo FROM tienda_online_categoria")).fetchall()
        print(f"\n Categorías registradas ({len(categorias)}):")
        for cat in categorias:
            print(f"  - [{cat.id}] {cat.nombre} (Activo: {bool(cat.activo)})")

        # Consultar productos cargados
        productos = conexion.execute(text("SELECT id, nombre, precio, stock FROM tienda_online_producto")).fetchall()
        print(f"\n Productos registrados ({len(productos)}):")
        for prod in productos:
            print(f"  - [{prod.id}] {prod.nombre} - Precio: ${prod.precio} | Stock: {prod.stock}")


if __name__ == "__main__":
    probar_conexion()

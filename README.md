# Tienda Online - Backend Django (IEI_N4_C3)

Sistema backend profesional desarrollado con **Python** y **Django** para la gestión de catálogo de productos, categorías, clientes, órdenes de compra/pedidos, métricas y autenticación de una plataforma de comercio electrónico.

---

## 1. Cumplimiento de Requerimientos y Evaluación 3

Este proyecto cumple de forma integral con todos los requerimientos acumulativos y los criterios de la **Evaluación N° 3 (CRUD mediante Class-Based Views - CBV)**:

1. **Requerimientos Acumulativos:**
   - Aislamiento de dependencias mediante entorno virtual (`.venv`).
   - Arquitectura desacoplada en dos aplicaciones: proyecto central (`drf`) y aplicación de negocio (`tienda_online`).
   - Plantilla base extensible (`base.html`) con barra de navegación unificada, mensajes flash y pie de página dinámico.
   - Manejo de archivos estáticos centralizados en `static/` (Bootstrap, DataTables, jQuery, imágenes).
   - Integración nativa con base de datos relacional MySQL (con fallback automático a SQLite en pruebas unitarias) mediante Django ORM.
   - Carga de datos iniciales (`datos_iniciales.json`) y script SQL [`script_base_datos.sql`](script_base_datos.sql).
   - Variables de entorno centralizadas mediante [.env](file:///.env) y `python-decouple`.
   - Django REST Framework (DRF) completamente operativo en `/api/`.

2. **CRUD Completo mediante Vistas Basadas en Clases (CBV):**
   - Implementación de las 5 vistas genéricas estándar de Django para cada entidad principal:
     - `ListView`: Listado tabular de registros con acciones y estados.
     - `DetailView`: Ficha técnica y visualización detallada del objeto individual.
     - `CreateView`: Alta de nuevos registros mediante formularios `ModelForm`.
     - `UpdateView`: Edición y actualización controlada de datos existentes.
     - `DeleteView`: Eliminación física con pantalla previa de confirmación (`confirm_delete`).
   - Cobertura total para las entidades **Producto**, **Categoría**, **Cliente** y **Pedido**.

3. **Formularios y Widgets Personalizados (`forms.py`):**
   - Arquitectura desacoplada de formularios en [`tienda_online/forms.py`](tienda_online/forms.py) mediante `forms.ModelForm`.
   - Definición explícita de campos (`fields = [...]`).
   - Widgets adaptados (`TextInput`, `EmailInput`, `NumberInput`, `Select`, `Textarea`, `CheckboxInput`) con atributos CSS (`form-control`, `form-select`), placeholders informativos, step decimal y restricciones de rango.

4. **Navegación e Interfaz Coherente:**
   - Menú de navegación global en [`tienda_online/templates/base.html`](tienda_online/templates/base.html) con acceso directo a todos los módulos.
   - Botones de acción contextuales en cada vista: *Volver al listado*, *Editar*, *Eliminar*, *Cancelar* y confirmaciones seguras.
   - Sin rutas huérfanas ni callejones sin salida; manejo de error 404 personalizado.

---

## 2. Justificación Técnica: Entidad `DetallePedido`

De acuerdo con el Criterio 2 de la rúbrica de evaluación:
> *"Sólo podrán omitirse vistas cuando exista una justificación técnica documentada en el README."*

### Justificación:
En el modelo relacional de comercio electrónico de este proyecto, la entidad `DetallePedido` (ítems de orden) representa las líneas de productos asociadas de manera dependiente y estricta a un `Pedido` padre:

1. **Integridad Referencial y Regla de Negocio:**
   Una línea de detalle no posee existencia independiente; requiere forzosamente una clave foránea hacia un `Pedido` existente (`on_delete=models.CASCADE`) y hacia un `Producto`. Permitir un CRUD independiente o descontextualizado para `DetallePedido` violaría la coherencia de negocio (permitiría crear líneas de venta sin orden asignada o alterar totales globales de compra de forma no controlada).

2. **Gestión Integrada en `Pedido`:**
   - La visualización de todas las líneas de detalle se encuentra integrada de forma directa y tabular dentro de la vista `PedidoDetailView` (`tienda_online/templates/tienda_online/pedidos/pedido_detail.html`), recorriendo `pedido.detalles.all`.
   - La eliminación de los detalles ocurre de forma atómica y en cascada a través de `PedidoDeleteView`, garantizando que no existan registros huérfanos en la base de datos.
   - Esta arquitectura responde al patrón de diseño de **Agregados (Domain-Driven Design / DDD)** donde el `Pedido` es la raíz del agregado que encapsula sus líneas de detalle.

---

## 3. Estructura del Proyecto

```text
IEI_N4_C3-main2/
├── .env                                    # Variables de entorno preconfiguradas
├── .gitignore                              # Archivos y carpetas excluidos de Git
├── manage.py                               # Utilidad CLI principal de Django
├── README.md                               # Documentación técnica completa
├── requirements.txt                        # Dependencias registradas del proyecto
├── script_base_datos.sql                   # Script SQL de creación y datos de prueba
├── conexion_sqlalchemy.py                  # Script de prueba de conexión directa
├── drf/                                    # Núcleo del proyecto Django (motor_django)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                         # Configuración global (DB, Static, Auth, Sesión, Fechas)
│   ├── urls.py                             # Enrutador principal y URLs de autenticación
│   └── wsgi.py
├── static/                                 # Archivos estáticos del proyecto
│   ├── css/                                # Hojas de estilo (bootstrap.css, datatables.css)
│   ├── js/                                 # Librerías JS (bootstrap.bundle, jquery, datatables)
│   └── images/                             # Recursos gráficos (logo.png)
└── tienda_online/                          # Aplicación del proyecto (mi_aplicacion)
    ├── admin.py                            # Registro de modelos en panel admin
    ├── apps.py                             # Metadatos de la aplicación
    ├── forms.py                            # Formularios ModelForm desacoplados con widgets
    ├── models.py                           # Modelos relacionales (Categoria, Producto, Cliente, Pedido, DetallePedido)
    ├── serializers.py                      # Serializadores DRF
    ├── tests.py                            # Suite de 31 pruebas unitarias automatizadas
    ├── urls.py                             # Mapa de rutas de todos los módulos CRUD CBV
    ├── views.py                            # CBV genéricas (ListView, DetailView, CreateView, UpdateView, DeleteView)
    ├── fixtures/
    │   └── datos_iniciales.json            # Fixture para precargar catálogo y registros
    └── templates/
        ├── 404.html                        # Plantilla personalizada para error 404
        ├── base.html                       # Plantilla base común con navegación universal
        ├── registration/                   # Plantillas de login y registro
        └── tienda_online/
            ├── bienvenida.html             # Página de bienvenida con accesos a módulos
            ├── vista_protegida.html        # Demostración de control de sesión
            ├── productos/                  # CRUD CBV de Producto
            │   ├── producto_list.html
            │   ├── producto_detail.html
            │   ├── producto_form.html
            │   └── producto_confirm_delete.html
            ├── categorias/                 # CRUD CBV de Categoría
            │   ├── categoria_list.html
            │   ├── categoria_detail.html
            │   ├── categoria_form.html
            │   └── categoria_confirm_delete.html
            ├── clientes/                   # CRUD CBV de Cliente
            │   ├── cliente_list.html
            │   ├── cliente_detail.html
            │   ├── cliente_form.html
            │   └── cliente_confirm_delete.html
            ├── pedidos/                    # CRUD CBV de Pedido
            │   ├── pedido_list.html
            │   ├── pedido_detail.html
            │   ├── pedido_form.html
            │   └── pedido_confirm_delete.html
            └── registros/                  # Vistas compatibles previas
```

---

## 4. Mapa Completo de Rutas CRUD (CBV)

### 4.1. Módulo Productos (`Producto`)
| Operación | URL | Vista CBV | Plantilla |
| :--- | :--- | :--- | :--- |
| **Listar** | `GET /productos/` | `ProductoListView` | `tienda_online/productos/producto_list.html` |
| **Detalle** | `GET /productos/<pk>/` | `ProductoDetailView` | `tienda_online/productos/producto_detail.html` |
| **Crear** | `GET, POST /productos/crear/` | `ProductoCreateView` | `tienda_online/productos/producto_form.html` |
| **Editar** | `GET, POST /productos/<pk>/editar/` | `ProductoUpdateView` | `tienda_online/productos/producto_form.html` |
| **Eliminar** | `GET, POST /productos/<pk>/eliminar/` | `ProductoDeleteView` | `tienda_online/productos/producto_confirm_delete.html` |

*(Rutas `/registros/` se mantienen activas como alias de compatibilidad).*

### 4.2. Módulo Categorías (`Categoria`)
| Operación | URL | Vista CBV | Plantilla |
| :--- | :--- | :--- | :--- |
| **Listar** | `GET /categorias/` | `CategoriaListView` | `tienda_online/categorias/categoria_list.html` |
| **Detalle** | `GET /categorias/<pk>/` | `CategoriaDetailView` | `tienda_online/categorias/categoria_detail.html` |
| **Crear** | `GET, POST /categorias/crear/` | `CategoriaCreateView` | `tienda_online/categorias/categoria_form.html` |
| **Editar** | `GET, POST /categorias/<pk>/editar/` | `CategoriaUpdateView` | `tienda_online/categorias/categoria_form.html` |
| **Eliminar** | `GET, POST /categorias/<pk>/eliminar/` | `CategoriaDeleteView` | `tienda_online/categorias/categoria_confirm_delete.html` |

### 4.3. Módulo Clientes (`Cliente`)
| Operación | URL | Vista CBV | Plantilla |
| :--- | :--- | :--- | :--- |
| **Listar** | `GET /clientes/` | `ClienteListView` | `tienda_online/clientes/cliente_list.html` |
| **Detalle** | `GET /clientes/<pk>/` | `ClienteDetailView` | `tienda_online/clientes/cliente_detail.html` |
| **Crear** | `GET, POST /clientes/crear/` | `ClienteCreateView` | `tienda_online/clientes/cliente_form.html` |
| **Editar** | `GET, POST /clientes/<pk>/editar/` | `ClienteUpdateView` | `tienda_online/clientes/cliente_form.html` |
| **Eliminar** | `GET, POST /clientes/<pk>/eliminar/` | `ClienteDeleteView` | `tienda_online/clientes/cliente_confirm_delete.html` |

### 4.4. Módulo Pedidos (`Pedido`)
| Operación | URL | Vista CBV | Plantilla |
| :--- | :--- | :--- | :--- |
| **Listar** | `GET /pedidos/` | `PedidoListView` | `tienda_online/pedidos/pedido_list.html` |
| **Detalle** | `GET /pedidos/<pk>/` | `PedidoDetailView` | `tienda_online/pedidos/pedido_detail.html` |
| **Crear** | `GET, POST /pedidos/crear/` | `PedidoCreateView` | `tienda_online/pedidos/pedido_form.html` |
| **Editar** | `GET, POST /pedidos/<pk>/editar/` | `PedidoUpdateView` | `tienda_online/pedidos/pedido_form.html` |
| **Eliminar** | `GET, POST /pedidos/<pk>/eliminar/` | `PedidoDeleteView` | `tienda_online/pedidos/pedido_confirm_delete.html` |

### 4.5. Rutas Generales, Autenticación y API
| URL | Vista | Descripción |
| :--- | :--- | :--- |
| `http://127.0.0.1:8000/` | `views.bienvenida` | Panel central interactivo de la aplicación. |
| `http://127.0.0.1:8000/login/` | `auth_views.LoginView` | Inicio de sesión con autenticación de Django. |
| `http://127.0.0.1:8000/logout/` | `auth_views.LogoutView` | Cierre de sesión seguro mediante POST. |
| `http://127.0.0.1:8000/registro/` | `views.registro` | Registro de usuarios nuevos mediante `ModelForm`. |
| `http://127.0.0.1:8000/protegida/` | `views.vista_protegida` | Acceso restringido por sesión (`@login_required`). |
| `http://127.0.0.1:8000/api/` | `router.urls` | Raíz de endpoints REST de Django REST Framework. |
| `http://127.0.0.1:8000/admin/` | `admin.site.urls` | Panel de administración oficial de Django. |
| `http://127.0.0.1:8000/404/` | `views.error_404` | Demostración de página no encontrada personalizada. |

---

## 5. Guía de Instalación y Puesta en Marcha

### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/47sophiv/Proyecto-backend-IEI-N4-C3.git
cd Proyecto-backend-IEI-N4-C3
```

### Paso 2: Crear y activar el ambiente virtual
- **Creación:**
  ```bash
  python -m venv .venv
  ```
- **Activación en Windows (PowerShell):**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
  *(Si PowerShell restringe la ejecución de scripts, ejecutar: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Bypass`)*

- **Activación en Windows (CMD):**
  ```cmd
  .\.venv\Scripts\activate.bat
  ```

### Paso 3: Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 4: Base de Datos MySQL y Migraciones
1. Importar el script SQL [`script_base_datos.sql`](script_base_datos.sql) en su gestor MySQL:
   ```bash
   mysql -u root -p < script_base_datos.sql
   ```
2. Ejecutar las migraciones de Django:
   ```bash
   python manage.py migrate
   ```

### Paso 5: Cargar datos iniciales (Fixtures)
```bash
python manage.py loaddata datos_iniciales.json
```

### Paso 6: Ejecutar el servidor de desarrollo
```bash
python manage.py runserver
```
Acceder a la aplicación web en: **`http://127.0.0.1:8000/`**

---

## 6. Pruebas Automatizadas (Unit Tests)

El proyecto cuenta con una suite completa de **31 pruebas unitarias** que verifican exhaustivamente:
- Modelos relacionales y métodos `__str__`.
- Validación de formularios `ModelForm` y widgets.
- Todas las operaciones CRUD mediante CBV (`ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`) para cada entidad.
- Control de autenticación, vistas protegidas y respuestas de error.

Para ejecutar la suite de pruebas:
```bash
python manage.py test
```
**Resultado esperado:**
```text
Ran 31 tests in ...s
OK
```
*(Nota: Durante la ejecución de `manage.py test`, Django utiliza automáticamente una base de datos SQLite en memoria para máxima velocidad y aislamiento).*

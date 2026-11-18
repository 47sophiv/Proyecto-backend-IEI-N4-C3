# Tienda Online - Backend Django (IEI_N4_C3)

Sistema backend profesional desarrollado con **Python** y **Django** para la gestión de catálogo, productos, clientes, pedidos, métricas y autenticación de una plataforma de comercio electrónico.

---

## 1. Propósito y Arquitectura del Proyecto

Este proyecto implementa la totalidad de los componentes solicitados en la guía curricular de backend con Django:
- **Aislamiento de dependencias:** Entorno virtual (`.venv`).
- **Arquitectura modular desacoplada:** Proyecto central (`drf`) y Aplicación del negocio (`tienda_online`).
- **Plantilla base (`base.html`):** Herencia modular mediante bloques (`{% block %}`) y consistencia de diseño visual.
- **Página de inicio y vista 404 personalizada:** Manejo de contexto dinámico y control global con `handler404`.
- **Manejo de archivos estáticos:** Directorio raíz `static/` organizado en `css/` (Bootstrap, DataTables), `js/` (Bootstrap bundle, jQuery, DataTables) e `images/` (`logo.png`).
- **Manejo de base de datos MySQL & ORM:** Integración nativa con Django ORM, conector `mysqlclient` y pruebas de conexión mediante `SQLAlchemy`.
- **Modelo de datos relacional:** Modelos `Categoria`, `Producto`, `Cliente`, `Pedido` y `DetallePedido`, con soporte de eliminación lógica (`habilitado`).
- **Carga de datos iniciales (Fixtures):** Archivo `datos_iniciales.json` para poblar la base de datos.
- **Desacople de datos sensibles:** Implementación de `python-decouple` y variables de entorno mediante [.env](file:///.env).
- **Django REST Framework (DRF):** Serializadores (`serializers.py`), vistas basadas en clase (`ModelViewSet`) y enrutador automático (`DefaultRouter`).
- **CRUD Manual tradicional:** Formularios `ModelForm` (`forms.py`), vistas genéricas CBV (`ListView`, `CreateView`, `UpdateView`, `DetailView`) y eliminación lógica mediante botón asíncrono `fetch` (`CambiarEstadoView`).
- **Autenticación, Sesiones y Registro:** Inicio de sesión (`LoginView`), cierre de sesión (`LogoutView`), registro de nuevos usuarios (`UserCreationForm`), variables de sesión (`request.session`), expiración de cookies y vistas protegidas (`@login_required`).
- **Control global de fechas:** Configuración de formatos en `settings.py` mediante diccionario `REST_FRAMEWORK`.

---

## 2. Estructura del Proyecto

```text
IEI_N4_C3-main2/
├── .env                                    # Variables de entorno preconfiguradas (público para evaluación)
├── .gitignore                              # Archivos y carpetas excluidos del control de versiones
├── manage.py                               # Utilidad de línea de comandos de Django
├── README.md                               # Documentación y guía completa de ejecución
├── requirements.txt                        # Dependencias registradas del proyecto
├── script_base_datos.sql                   # Script SQL de creación de base de datos, tablas y datos iniciales
├── conexion_sqlalchemy.py                  # Script de prueba de conexión directa mediante SQLAlchemy
├── drf/                                    # Núcleo del proyecto Django (motor_django)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                         # Configuración global (DB, Static, Auth, Sesión, Fechas)
│   ├── urls.py                             # Enrutador principal y URLs de autenticación
│   └── wsgi.py
├── static/                                 # Archivos estáticos del proyecto
│   ├── css/
│   │   ├── bootstrap.css                   # Estilos principales de diseño
│   │   └── datatables.css                  # Estilos de tablas de datos
│   ├── js/
│   │   ├── bootstrap.bundle.js             # Scripts y componentes interactivos
│   │   ├── jquery_v4.0.0.js                # Librería jQuery
│   │   └── datatables.js                   # Funcionalidades de tablas
│   └── images/
│       └── logo.png                        # Logotipo e icono institucional
└── tienda_online/                          # Aplicación del proyecto (mi_aplicacion)
    ├── __init__.py
    ├── admin.py                            # Registro de modelos en el panel de administración
    ├── apps.py                             # Configuración y metadatos de la aplicación
    ├── forms.py                            # Formularios ModelForm (ProductoForm, CambiarEstadoForm)
    ├── models.py                           # Modelos relacionales con campo habilitado
    ├── serializer.py                       # Serializadores DRF (ModelSerializer)
    ├── serializers.py                      # Reexportación de serializadores
    ├── tests.py                            # Suite de pruebas unitarias automatizadas
    ├── urls.py                             # Rutas de la app (Bienvenida, CRUD, DRF API, 404)
    ├── views.py                            # Controladores (Bienvenida, CRUD CBV, DRF ViewSets, Auth)
    ├── fixtures/
    │   └── datos_iniciales.json            # Fixture para precargar catálogo y registros
    └── templates/
        ├── 404.html                        # Plantilla personalizada para error 404
        ├── base.html                       # Plantilla base común con navegación y sesión
        ├── registration/                   # Plantillas del sistema de autenticación
        │   ├── login.html                  # Formulario de inicio de sesión
        │   └── registro.html               # Formulario de creación de cuenta de usuario
        └── tienda_online/
            ├── bienvenida.html             # Página de bienvenida interactiva
            ├── vista_protegida.html        # Demostración de acceso protegido por sesión
            └── registros/                  # Vistas del CRUD manual tradicional
                ├── lista_registros.html    # ListView con tabla y botón cambiar-estado
                ├── crear_registro.html     # CreateView con formulario ModelForm
                ├── editar_registro.html    # UpdateView para modificar el registro
                └── detalle_registro.html   # DetailView con información del producto
```

---

## 3. Guía de Instalación y Ejecución

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

### Paso 4: Base de Datos MySQL
1. Importar el script SQL [`script_base_datos.sql`](script_base_datos.sql) en MySQL (workbench o consola):
   ```bash
   mysql -u root -p < script_base_datos.sql
   ```
2. Ejecutar las migraciones pendientes en Django:
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
El servidor estará accesible en: `http://127.0.0.1:8000/`

---

## 4. Mapa de Rutas de la Aplicación

| URL | Vista / Método | Propósito |
| :--- | :--- | :--- |
| `http://127.0.0.1:8000/` | `bienvenida` | Página principal de bienvenida con catálogo de módulos y estado del servidor. |
| `http://127.0.0.1:8000/registros/` | `RegistroListView` | Listado general de productos con estado y acciones. |
| `http://127.0.0.1:8000/registros/crear/` | `RegistroCreateView` | Formulario para agregar un nuevo producto. |
| `http://127.0.0.1:8000/registros/<id>/editar/` | `RegistroUpdateView` | Formulario para editar un producto existente. |
| `http://127.0.0.1:8000/registros/<id>/detalle/` | `RegistroDetailView` | Vista detallada de un producto individual. |
| `http://127.0.0.1:8000/registros/<id>/cambiar_estado/` | `CambiarEstadoView` | Endpoint AJAX POST para habilitar/deshabilitar (eliminación lógica). |
| `http://127.0.0.1:8000/login/` | `auth_views.LoginView` | Inicio de sesión de usuarios con redirección a `/`. |
| `http://127.0.0.1:8000/logout/` | `auth_views.LogoutView` | Cierre de sesión y limpieza de la sesión en base de datos. |
| `http://127.0.0.1:8000/registro/` | `views.registro` | Registro de nuevos usuarios mediante `UserCreationForm`. |
| `http://127.0.0.1:8000/protegida/` | `views.vista_protegida` | Vista de demostración protegida mediante `@login_required`. |
| `http://127.0.0.1:8000/api/` | `router.urls` | Raíz de la API navegable de Django REST Framework. |
| `http://127.0.0.1:8000/admin/` | `admin.site.urls` | Panel de administración de Django. |
| `http://127.0.0.1:8000/404/` | `views.error_404` | Verificación directa de la plantilla 404 personalizada. |

---

## 5. Pruebas Automatizadas (Unit Tests)

Para ejecutar la suite completa de pruebas unitarias:
```bash
python manage.py test
```
Verifica la creación y representación de modelos, las vistas CRUD manuales, el cambio dinámico de estado (habilitado/deshabilitado), la autenticación de usuarios y las respuestas HTTP.

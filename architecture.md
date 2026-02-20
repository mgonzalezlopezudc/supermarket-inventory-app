# Arquitectura de la Aplicación

## 1. Stack Tecnológico
- **Backend:** Python + Flask. Proporciona las directivas de enrutamiento y API.
- **Base de Datos:** SQLite con SQLAlchemy (como ORM para Python) por su rapidez y menor curva de configuración para proyectos manejables o despliegues rápidos.
- **Frontend:** Jinja2 para la plantilla HTML renderizada desde el servidor + Vanilla CSS moderno. JavaScript vanilla para interacciones y operaciones CRUD asíncronas vía Fetch API (opcionalmente) o mediante formularios estándar.
- **Internacionalización (i18n):** Flask-Babel para el soporte multilingüe inglés/español.
- **Pruebas (Testing):** `pytest` como motor de ejecución para las pruebas unitarias y de integración.

## 2. Patrón de Diseño
La aplicación sigue el patrón **MVC (Model-View-Controller)**:
- **Modelo (Model):** Definidos mediante SQLAlchemy en `models.py`. Encapsula Store, Product, Shelf e InventoryItem.
- **Vista (View):** Plantillas en la carpeta `templates/` con bloques modulares en Jinja2 (`base.html`, `dashboard.html`, `stores.html`, etc.).
- **Controlador (Controller):** Lógica y rutas definidas en `app.py` y opcionalmente en blueprints si la aplicación crece. Gestiona las peticiones de los usuarios.

## 3. Estructura de Directorios (Propuesta)
```
/
├── app.py              # Controlador principal de la aplicación Flask
├── models.py           # Definición de modelos SQLAlchemy (Store, Product, etc.)
├── generate_data.py    # Script para popular la BD con los datos de prueba
├── requirements.txt    # Dependencias de Python
├── static/
│   ├── css/
│   │   └── style.css   # CSS base para glassmorphism/dark mode
│   └── js/
│       └── main.js     # Script para manejo del modal CRUD y utilidades
├── templates/
│   ├── base.html       # Esqueleto HTML de la aplicación
│   ├── dashboard.html  # Vista Global
│   ├── stores/
│   │   ├── index.html  # Listado de tiendas
│   │   └── detail.html # Detalle de tienda (lista de productos en ella)
│   └── products/
│       ├── index.html  # Listado de productos
│       └── detail.html # Detalle de producto (dónde está disponible)
└── tests/              # Pruebas automatizadas (pytest)
    ├── conftest.py     # Configuración y fixtures compartidos de pytest
    ├── test_models.py  # Pruebas unitarias de modelos DB e integridad referencial
    └── test_routes.py  # Pruebas de integración sobre los endpoints de la API Flask
```

## 4. Flujos Clave
- **Carga de Test:** En el arranque, comprobar si la BD está vacía y llamar a la función generadora de datos si fuera necesario.
- **Multilenguaje:** El usuario podrá cambiar en la interfaz (ej. header) o según preferencias del navegador. Flask-Babel intercepta la petición y formatea el contenido estático.
- **Visualización:** El CSS y las transiciones usarán variables CSS y un estilo "premium", evitando diseños tipo bootstrap 3.

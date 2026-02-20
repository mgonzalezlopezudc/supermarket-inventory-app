# Project Setup: Supermarket Inventory App

A continuación se adjuntan los documentos fundamentales para la configuración y desarrollo del proyecto:

<details>
<summary><b>1. TASK.md (Planificación)</b></summary>

# Aplicación de Gestión de Inventario de Supermercado

- [x] Planificar la arquitectura de la aplicación y PRD
  - [x] Crear `PRD.md`
  - [x] Crear `architecture.md`
  - [x] Crear `AGENTS.md`
- [ ] Inicializar el proyecto Flask
  - [ ] Configurar `app.py`, `models.py`, `views.py`
  - [ ] Configurar i18n (Babel) con idiomas EN y ES
- [ ] Implementar modelos de datos y datos de prueba
  - [ ] Store, Product, Shelf, InventoryItem
  - [ ] Generar 4 tiendas, 4 baldas/tienda, 10 productos, 2 productos/balda
- [ ] Implementar vistas backend y CRUD
  - [ ] Dashboard
  - [ ] Listado y detalle de tiendas (Stores)
  - [ ] Listado y detalle de productos (Products)
  - [ ] Controladores para operaciones CRUD
- [ ] Diseñar e implementar el frontend
  - [ ] CSS moderno y altamente visual (dark mode, glassmorphism)
  - [ ] Plantillas Jinja2 para todas las vistas
- [ ] Implementar pruebas automáticas
  - [ ] Pruebas unitarias de modelos y utilidades
  - [ ] Pruebas de integración de rutas y vistas con cliente de prueba Flask
- [ ] Verificar la funcionalidad

</details>


<details>
<summary><b>2. implementation_plan.md</b></summary>

# Plan de Implementación de la Aplicación de Inventario

## Cambios Propuestos
### Configuración del Backend
#### [NEW] `app.py`
- Inicialización de la aplicación Flask
- Configuración de i18n usando Flask-Babel
- Configuración de la base de datos SQLite
- Rutas para el Dashboard, Tiendas (Stores), Productos y operaciones CRUD

#### [NEW] `models.py`
- Modelos SQLAlchemy: `Store`, `Product`, `Shelf`, `InventoryItem`

#### [NEW] `generate_data.py`
- Script para poblar la base de datos con los datos de prueba solicitados (4 tiendas, 4 baldas/tienda, 10 productos, 2 productos/balda con imágenes representativas).

### Configuración del Frontend
#### [NEW] `style.css`
- CSS moderno y muy visual, utilizando modo oscuro, glassmorphism, acentos brillantes y diseño responsive.

#### [NEW] `base.html`
- Plantilla base de Jinja2 con navegación integrada y selector de idioma (EN/ES).

#### [NEW] Vistas Jinja2
- **Dashboard:** `templates/dashboard.html` para métricas globales.
- **Tiendas:** `templates/stores_index.html` y `templates/store_detail.html`
- **Productos:** `templates/products_index.html` y `templates/product_detail.html`

### Configuración de Pruebas
#### [NEW] `conftest.py`
- Configuración global de `pytest`, incluyendo cliente de prueba Flask (`test_client`) y acceso a la base de datos de pruebas en memoria (`sqlite:///:memory:`).

#### [NEW] `test_models.py`
- **Pruebas Unitarias:** Verificación de la creación de las entidades, relaciones (ej. borrado en cascada) y guardado en base de datos.

#### [NEW] `test_routes.py`
- **Pruebas de Integración:** Realización de peticiones HTTP al `test_client` para validar respuestas (cód. 200, 404, etc.) en los diferentes endpoints.

## Plan de Verificación
### Verificación Manual
- Ejecutar `python generate_data.py` seguido de `python app.py`.
- Navegar en el explorador para verificar la estética visual premium (modo oscuro/glassmorphism).
- Probar las 3 vistas requeridas (Dashboard, Tiendas, Productos) para asegurar que cargan y se enlazan correctamente.
- Ejecutar operaciones CRUD básicas en una Tienda/Producto.
- Cambiar el idioma mediante la interfaz de usuario para verificar que las traducciones de Flask-Babel (Inglés/Español) se aplican automáticamente.

</details>

<details>
<summary><b>3. PRD.md</b></summary>

# Product Requirements Document (PRD)

## 1. Objetivo del Producto
Desarrollar una aplicación web de gestión de inventario para una cadena de supermercados. La aplicación permitirá visibilizar el estado del inventario de forma global, por tiendas y por productos, facilitando la toma de decisiones y el control de stock mediante una interfaz moderna y atractiva.

## 2. Usuarios Objetivo
- **Gestores de inventario:** Necesitan ver el stock disponible en cada tienda, qué productos están en qué baldas y manejar la reposición.
- **Administradores:** Encargados de definir tiendas, baldas y el catálogo de productos.

## 3. Funcionalidades Principales (Alcance)
1. **Dashboard Global:** Vista resumen del estado del inventario a nivel cadena.
2. **Gestión de Tiendas (Stores):** Listado de tiendas con vista detalle (sus productos y stock).
3. **Gestión de Productos (Products):** Listado del catálogo con vista detalle (en qué tiendas y baldas está cada producto).
4. **Operaciones CRUD:** Capacidad de Crear, Leer, Actualizar y Eliminar (Create, Read, Update, Delete) para cada entidad.
5. **Multi-idioma (i18n):** Soporte en idioma Español e Inglés.

## 4. Modelo de Datos
- **Store:** `id`, `name`, `image` (URL), `address`, `location` (geoJson)
- **Product:** `id`, `name`, `image` (URL), `size`, `price`
- **Shelf:** `id`, `name`, `capacity`, `refStore` (clave foránea a Store)
- **InventoryItem:** `id`, `refProduct`, `refStore`, `refShelf`, `qty` (cantidad en la balda), `qty_total` (cantidad total en la tienda)

## 5. Requisitos No Funcionales
- **Estética:** Moderna y muy visual (Glassmorphism, Dark mode, colores vibrantes).
- **Tecnología:** Flask + Jinja2 + Vanilla CSS moderno.
- **Datos de prueba:** Generar 4 tiendas (cada una con 4 baldas), 10 productos (al menos 2 productos por balda). Imágenes representativas mediante URLs (ej. Unsplash source).

</details>

<details>
<summary><b>4. architecture.md</b></summary>

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

</details>

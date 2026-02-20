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

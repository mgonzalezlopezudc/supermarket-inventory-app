# Agentes de la Arquitectura (AGENTS.md)

En el contexto de la aplicación, podemos definir diferentes *"Agentes"* lógicos o responsabilidades de sistema que interactúan para que la plataforma funcione. 

## 1. Data Agent (Gestor de Datos)
- **Rol:** Interactúa con el ORM (SQLAlchemy) para realizar consultas (`Queries`) y persistir datos.
- **Responsabilidad:** Garantizar la integridad referencial (ej., eliminar una balda borra sus InventoryItems). Generación de los datos semilla (Seed Data Agent).

## 2. Router / View Agent (Enrutador Web)
- **Rol:** Punto de entrada a las solicitudes del usuario (Navegador).
- **Responsabilidad:** Entender la URL solicitada, invocar al Data Agent si necesita información, y pasar los datos resultantes al Render Agent para entregar la respuesta.

## 3. UI/Render Agent (Gestor de Presentación)
- **Rol:** Jinja2 Engine + Estilos CSS.
- **Responsabilidad:** Tomar datos puros y aplicar las plantillas correspondientes para retornar HTML bien formado. Se encarga de traducir textos utilizando Babel.

## 4. Internationalization Agent (Babel / i18n)
- **Rol:** Intérprete del idioma seleccionado por el usuario.
- **Responsabilidad:** Interceptar las etiquetas de localización en Jinja2 (ej: `{{ _('Dashboard') }}`) y devolver el texto en el idioma activo (Español o Inglés).

## 5. REGLAS DE DESARROLLO (DEVELOPMENT RULES)
- Los archivos `TASK.md` y `implementation_plan.md` generados en el contexto del agente/asistente SIEMPRE deben generarse y actualizarse en **CASTELLANO**.
- El entorno virtual de desarrollo en Python debe llamarse siempre **`.venv`** (nunca `venv`). Este agente, cuando genere comandos de script, se asegurará de apuntar siempre a `source .venv/bin/activate`.
- Al inicializar y trabajar con repositorios **Git**, la rama principal a utilizar será siempre **`main`** (en lugar de `master`).

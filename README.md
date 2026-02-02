# FastAPI Media Engine 🚀

Este proyecto es una aplicación backend de grado de producción diseñada para gestionar la subida, transformación y entrega de imágenes y videos. Implementado con **FastAPI**, el framework de Python de alto rendimiento, el sistema está optimizado para la eficiencia y la seguridad.

Este repositorio forma parte de mi formación intensiva para convertirme en **AI Engineer**, enfocándome en la creación de APIs robustas que sirvan como infraestructura para modelos multimodales.

## 🛠️ Stack Tecnológico

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Asíncrono por defecto).
- **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/) con soporte `asyncio`.
- **Autenticación:** JWT (JSON Web Tokens) mediante `fastapi-users`.
- **Gestión Multimedia:** [ImageKit.io](https://imagekit.io/) para CDN, optimización y transformaciones en tiempo real.
- **Base de Datos:** SQLite (desarrollo) / Soporte para PostgreSQL.
- **Gestor de Paquetes:** `uv` (moderno y extremadamente rápido).

## ✨ Características Principales

- **Gestión de Usuarios:** Registro, login y protección de rutas mediante Bearer Tokens.
- **Pipeline Multimedia:**
  - Subida asíncrona de imágenes y videos.
  - Transformaciones automáticas (redimensionado, marcas de agua, filtros de contraste) mediante parámetros de URL.
  - Almacenamiento optimizado en la nube.
- **Arquitectura Limpia:** Separación de responsabilidades en `schemas`, `db`, `users` e `images`.
- **Documentación Automática:** Swagger UI disponible en `/docs` para testeo inmediato.

## 📂 Estructura del Proyecto

```text
src/
├── app/
│   ├── app.py        # Punto de entrada y definición de rutas
│   ├── db.py         # Configuración de base de datos y modelos
│   ├── schemas.py    # Modelos de validación Pydantic
│   ├── users.py      # Lógica de autenticación y gestión de usuarios
│   └── images.py     # Integración con ImageKit SDK
├── .env              # Variables de entorno (Keys de ImageKit)
└── main.py           # Lanzador del servidor Uvicorn
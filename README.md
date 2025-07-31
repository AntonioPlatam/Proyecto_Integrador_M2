# Proyecto Integrador M2: Modelado de Datos para E-Commerce

Este repositorio alberga el desarrollo del "Proyecto Integrador del Módulo 2", cuyo objetivo es optimizar una plataforma de comercio electrónico a través del diseño e implementación de una arquitectura de datos dimensional utilizando herramientas modernas de ingeniería de datos.

# Contenido de proyecto
```
└── 📁PI2_M2
    └── 📁Avance_1
        └── 📁data
            ├── 10.ordenes_metodospago.sql
            ├── 11.resenas_productos.sql
            ├── 12.historial_pagos.sql
            ├── 2.usuarios.sql
            ├── 3.categorias.sql
            ├── 4.Productos.sql
            ├── 5.ordenes.sql
            ├── 6.detalle_ordenes.sql
            ├── 7.direcciones_envio.sql
            ├── 8.carrito.sql
            ├── 9.metodos_pago.sql
        └── 📁orm
            └── 📁__pycache__
                ├── db_conector.cpython-313.pyc
                ├── modelos.cpython-313.pyc
            ├── crear_tablas.py
            ├── db_conector.py
            ├── modelos.py
        ├── exporacion.ipynb
        ├── README.md
    └── 📁Avance_2
    └── 📁Avance_3
    └── 📁dbt_profiles
        ├── profiles.yml
    └── 📁logs
        ├── dbt.log
    ├── .env
    ├── docker-compose.yml
    ├── Dockerfile
    └── README.md
```


## Descripción de la Estructura

Este proyecto está organizado en avances progresivos, cada uno enfocado en diferentes aspectos del modelado dimensional:

### 📂 **Avance_1**
- **`data/`**: Scripts SQL para la creación e inserción de datos en las tablas del e-commerce (usuarios, productos, órdenes, etc.)
- **`orm/`**: Módulo Python con SQLAlchemy para la conexión a base de datos y definición de modelos
- **`exporacion.ipynb`**: Notebook para análisis exploratorio y conexión a la base de datos

### 📂 **Avance_2 & Avance_3**
- Directorios preparados para las siguientes fases del proyecto (transformaciones y análisis avanzado)

### 📂 **dbt_profiles/**
- Configuración de perfiles para dbt (data build tool) para transformaciones de datos

### 🔧 **Archivos de configuración**
- **`.env`**: Variables de entorno para conexión a base de datos
- **`docker-compose.yml`**: Configuración para levantar PostgreSQL y pgAdmin en contenedores
- **`Dockerfile`**: Imagen personalizada para el entorno de desarrollo
- **`logs/`**: Registros de ejecución de dbt

### 🎯 **Objetivo**
La estructura permite un desarrollo incremental desde la creación de la base de datos (Avance 1) hasta la implementación completa del modelo dimensional y análisis de datos.


## 🐳 Guía Rápida - Configuración Docker

### Prerrequisitos
- Docker Desktop instalado y ejecutándose

#### 1. **Verificar archivo .env**
Asegúrase de que el archivo `.env` tenga estas configuraciones:
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ecommercedb
DB_USER= #Usuario
DB_PASSWORD=#Password

PGADMIN_DEFAULT_EMAIL= #Email para ingresar a pgadmin
PGADMIN_DEFAULT_PASSWORD= #Password para ingresar a pgadmin
```

### Desde la carpeta raíz del proyecto (donde está docker-compose.yml)
```
docker-compose up -d
```

### Ver el estado de los contenedores
```
docker-compose ps
```

### Acceder a los servicios
```
PostgreSQL: localhost:5432
pgAdmin: http://localhost:8080
Email: #Email para ingresar a pgadmin
Password: #Password para ingresar a pgadmin
```

✅ ¡Listo!
Una vez que docker-compose ps muestre los contenedores como "Up" ya esta listo nuestro Contenedor de docker.


> 📋 Para más detalles sobre el Avance 1, consulta: [Avance_1/README.md](./Avance_1/README.md)
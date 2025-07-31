# Avance 1 del Proyecto Integrador M2

**Fase:** Avance 1 - Carga y Entendimiento de los Datos.

### PI 1: Configuración del Entorno de Trabajo

**a. Instalación y Configuración:**

Se realizó una adaptación de los archivos .sql originales, los cuales estaban escritos en sintaxis T-SQL (específica para Microsoft SQL Server). Para garantizar la compatibilidad con PostgreSQL, se normalizaron los nombres de columnas y tablas al formato "snake_case" y se ajustó la sintaxis SQL correspondiente, permitiendo así la correcta inserción de datos en el entorno PostgreSQL configurado.

**b. Creación de Base de Datos y Conexión ORM:**

Se creó la base de datos `ecommerceDB` en `PostgreSQL`. Se desarrolló un script en Python usando `SQLAlchemy` y `pg8000` para conectarse a la base de datos. Esta conexión permite automatizar la carga de datos y realizar análisis exploratorios.

### PI 2: Carga Inicial de Datos

El proceso de carga inicial se divide en dos fases principales. Primero, se ejecuta el script `crear_tablas.py` que utiliza SQLAlchemy para generar automáticamente todas las tablas del modelo de datos basado en las definiciones de los modelos ORM.

```bash
cd Avance_1/orm
python crear_tablas.py
```

 Esto creará el modelo de base de datos dentro de nuestro servidor PostgreSQL

### Poblar las tablas con datos
Una vez creadas las tablas, ejecuta los scripts SQL de la carpeta `data/` para poblar las tablas con datos de ejemplo:

```bash
# Navegar a la carpeta de datos
cd Avance_1/data

# Ejecutar los scripts en orden (o conectarse via pgAdmin)
# Puedes usar psql o ejecutarlos directamente en pgAdmin
```

### PI 3: Tratamiento de Campos Semi-estructurados

**a. Identificación de Columnas:**

Después de realizar un análisis exhaustivo del esquema de datos y el contenido de todas las tablas del sistema e-commerce, se determinó que **no se encontraron columnas que contengan datos en formato JSON o estructuras de listas anidadas**. 

Todas las columnas identificadas siguen un formato de datos estructurado tradicional (enteros, strings, fechas, decimales, booleanos), lo que simplifica el proceso de análisis y transformación de datos. Esta característica del dataset facilita las operaciones de consulta y manipulación de datos sin requerir técnicas especializadas para el tratamiento de datos semi-estructurados.

**b. Aplicación de Técnicas de Limpieza:**

Dado que no se identificaron campos semi-estructurados en el dataset, **no fue necesario aplicar técnicas específicas de limpieza para datos JSON o listas anidadas**. 

Los datos ya se encuentran en un formato estructurado y normalizado que cumple con los estándares de bases de datos relacionales. Las únicas transformaciones realizadas fueron:

- Normalización de nombres de columnas y tablas al formato "snake_case"
- Adaptación de sintaxis SQL de T-SQL a PostgreSQL
- Verificación de tipos de datos y restricciones de integridad

Esta estructura de datos facilita directamente el proceso de análisis exploratorio y la posterior implementación del modelo dimensional.


### PI 4: Análisis Exploratorio y Evaluación de Calidad de Datos

**a. Herramientas Utilizadas:**

El análisis exploratorio se realizó utilizando un Jupyter Notebook (`exporacion.ipynb`) 

**b. Metodología de Análisis:**

Se implementó un enfoque sistemático que incluye:

1. **Análisis de estructura:** Revisión de esquemas, tipos de datos y relaciones entre tablas
2. **Evaluación de completitud:** Identificación de valores nulos y faltantes por columna
3. **Análisis de consistencia:** Verificación de formatos de datos y restricciones de integridad

**c. Resultados del Análisis:**

 **Ejecutar el notebook para ver resultados detallados:**
```bash
# Abrir Jupyter Notebook
jupyter notebook Avance_1/exporacion.ipynb
```

> **[Ver Avance 2: Modelo Dimensional](../Avance_2/README.md)**

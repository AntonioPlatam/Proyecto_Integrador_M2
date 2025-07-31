#  nforme Técnico: Avance 3 del Proyecto Integrador

## 1. Descripción General

En esta etapa del proyecto se implementó un flujo de transformación de datos automatizado con **DBT**, basado en un **modelo estrella** diseñado previamente.  
El objetivo fue estructurar datos provenientes de archivos CSV planos hacia un esquema optimizado para análisis, garantizando **integridad referencial** y **trazabilidad**.

### PI 1: Implementación del Modelo Físico

La implementacion del modelo fisico consiste en las tablas de hechos y dimensiones antes generadas, se genero un script de SQL para la creacion de las tablas definiendo las columnas, tipos de datos, etc. Todo deacuerdo al diseño logico propuesto.

### PI 2: Creación de Scripts de Transformación en DBT


a transformación de datos se organizó en tres capas, utilizando la convención de **arquitectura medallón**:

### a. Staging (Bronce): Preparación Inicial

Los modelos `stg_*` fueron creados para estandarizar los datos extraídos de fuentes CSV.

- **Limpieza aplicada:**  

  - Renombrado uniforme de campos (`snake_case`)  
  - Corrección de tipos (por ejemplo, fechas a `DATE` y montos a `DECIMAL`)

---

### b. Intermedios (Plata): Enriquecimiento y normalización

En esta capa se aplicaron validaciones adicionales y transformaciones lógicas:

- Unión entre direcciones y usuarios para enriquecer clientes.
- Conversión de códigos de país a nombre completo.
- Validación de rangos de fechas para asegurar consistencia temporal.

---

### c. Modelos Analíticos (Oro): Dimensiones y hechos finales

- **`dim_clientes`**: Incluye tanto datos personales como de ubicación. Implementa SCD Tipo 2 con campos `fecha_inicio` y `fecha_fin`.
- **`dim_productos`**: Abarca detalles de productos y su categoría. Algunos atributos, como `estado`, se tratan como SCD Tipo 1.
- **`fct_ventas`**: Resume transacciones, enlazando con claves foráneas. Calcula `monto_total` a partir de `cantidad_vendida` y `precio_por_unidad`.

Todos los modelos finales se materializaron como **tablas** para mejorar la eficiencia de consultas analíticas.


### PI 3: Manejo de Relaciones en DBT

Para garantizar relaciones sólidas entre modelos, se utilizaron las siguientes prácticas:

- `source()` para declarar archivos fuente.
- `ref()` para relacionar modelos entre capas, lo que permitió a DBT construir un **grafo de ejecución** que asegura el orden correcto de construcción.
- **Pruebas automáticas (`tests`)** para verificar:
  - Unicidad de claves primarias
  - Existencia de claves foráneas
  - Integridad de relaciones



### PI 4: Presentación de Insights (Storytelling)
Después de limpiar las tablas y transformarlos usando DBT, ya contamos con una tabla `fct_ventas` más confiable y ordenada. Esto nos permite hacer análisis más claros para entender mejor qué está pasando con las ventas del negocio.

A continuación se muestran dos consultas que nos ayudan a obtener insights importantes usando SQL sobre el modelo dimensional.

**Consulta 1: Productos que generan más ingresos**
```sql
SELECT
    p.nombre_producto,
    SUM(f.monto_total) AS ingresos_totales
FROM fact_ventas f
JOIN dim_productos p ON f.producto_id = p.id
GROUP BY p.nombre_producto
ORDER BY ingresos_totales DESC
LIMIT 5;
```

Esta consulta nos muestra los cinco productos que más dinero han generado. Saber esto es útil para que el negocio sepa en qué productos enfocarse, ya sea para promocionarlos más o asegurarse de tener suficiente inventario.

**Consulta 2: Ingresos por mes**
```sql
SELECT
    df.año,
    df.mes,
    SUM(f.monto_total) AS ingresos_mensuales
FROM fact_ventas f
JOIN dim_fecha df ON f.fecha_id = df.id
GROUP BY df.año, df.mes
ORDER BY df.año, df.mes;
```

Esta consulta ayuda a ver cómo cambian las ventas mes con mes. Con eso, podemos detectar si hay meses donde se vende más (por ejemplo, en temporadas altas) o si hay caídas en ciertas épocas del año.
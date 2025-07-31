# Avance 2: Diseño del Modelo de Datos

### PI 1: Análisis de Negocio y Descubrimiento de Requisitos

Para el diseño efectivo del modelo dimensional, es fundamental comprender qué quiere resolver el negocio y qué datos están disponibles para ello. A continuación se presentan las preguntas de negocio clave que guiarán el diseño del modelo de datos:

**a. Preguntas de Negocio Principales**

**Análisis de Ventas:**
* ¿Cuáles son los productos más vendidos por categoría?
* ¿Cuáles son los métodos de pago más utilizados por los clientes?

**Análisis de Clientes:** 
* ¿Cuál es el perfil demográfico de los clientes más valiosos?

**Análisis Financiero:**
* ¿Cuáles son los ingresos totales por mes, trimestre y año?
* ¿Cuál es el ticket promedio por cliente?

**Analisis Producto**
* ¿Qué productos generan mayor margen de ganancia?

**b. Entendimiento de datos y requisitos**

Como se identificó en el avance anterior, se cuenta con la información necesaria para responder a las principales preguntas del negocio. Estas preguntas están orientadas a analizar los aspectos clave del proceso de ventas en el contexto de un sistema de comercio electrónico.

El modelo dimensional se ha diseñado considerando los elementos fundamentales que todo análisis debe responder:

- **¿Quién?** → Información disponible en la tabla `usuarios`
- **¿Cuándo?** → A través del campo `fecha_orden`
- **¿Dónde?** → Mediante la tabla `direccion_envio`
- **¿Qué?** → Detallado en la tabla `productos`

Gracias a esta estructura, el modelo permite obtener una visión clara y organizada del comportamiento del negocio, facilitando el análisis de ventas, clientes y finanzas con base en hechos y dimensiones bien definidas.


### PI 2: Identificación de Componentes del Modelo Dimensional

**a. Identificación de Hechos (Hechos):**

El proceso de negocio modelado es **Ventas**, y las métricas cuantitativas (hechos) que se desean analizar son las siguientes:

- `CantidadVendida`: Número de unidades de un producto incluidas en cada línea de una orden.
- `PrecioPorUnidad`: Precio del producto en el momento en que se realiza la venta.
- `MontoTotal`: Resultado de `CantidadVendida * PrecioPorUnidad`. Esta es la métrica principal y completamente aditiva.
- `Ubicacion`: Zona geografica donde se realizo la compra.


**b. Determinación de Dimensiones (Filtros y Agrupaciones):**
La tablas de dimensiones nos permiten tener informacion detallada, este tipo de tablas reponderian las preguntas del punto anterior como el quien, donde, cuando, el que de nuestra tabla de hechos Ventas

Las tablas de dimensiones sugeridas para desarrollar el **Ventas** son las siguientes:
* **Dimensión Cliente (`dim_clientes`):** Describe al cliente que realiza la compra
* **Dimensión Producto (`dim_productos`):** Describe el producto que se vende.
* **Dimensión Tiempo (`dim_fecha`):** Describe la fecha exacta de la venta, permitiendo agrupaciones por día, mes, año, etc. 
* **Dimensión Geografía (`dim_ubicaciones`):** Describe la ubicación de envío del pedido.

### PI 3: Diseño del Modelo de Datos

**a. Diseño Conceptual y Lógico:**

![Diagrama ER](../docs/assets/diagrama_er.png)

Este repositorio incluye el diseño entidad-relación (ER) de una base de datos orientada a un sistema de comercio electrónico. El diagrama organiza y diferencia claramente entre:

-  **Tablas de hechos** (color rosa): representan actividades o transacciones que ocurren en el sistema.
            - `ordenes`
            - `carrito`
            - `resenas_producto`
            - `orden_metodos_pago`
            - `historial_pagos`

- **Tablas de dimensiones** (color azul): contienen información descriptiva relacionada con las transacciones.
      - `usuarios`
      - `productos`
      - `categorias`
      - `metodos_pagos`
      - `direccion_envio`

El modelo establece relaciones clave entre entidades como usuarios, productos, órdenes, métodos de pago y direcciones de envío, garantizando la **integridad referencial** y la **trazabilidad de los datos** en todo el sistema.

El diagrama proporciona una base sólida para el desarrollo de consultas, reportes y funcionalidades dentro del sistema de e-commerce.


**b. Modelar Slowly Changing Dimensions (SCDs)**

Para manejar los cambios en las dimensiones a lo largo del tiempo, se implementan diferentes estrategias SCD según la criticidad del historial de datos:


**SCD TIPO 1 DIM_UBICACION (dim_ubicacion):**
- **Campos afectados:** Información geográfica (ciudad, estado, código postal)
- **Justificación:** Los cambios en datos geográficos son correcciones administrativas, no requieren historial
- **Ejemplo:** Corrección de código postal de "82104" a "82120"


**SCD tipo 2  DIM_CLIENTE (dim_cliente):**
- **Campos de control:** 
  - `fecha_inicio` (fecha de vigencia del registro)
  - `fecha_fin` (fecha de finalización)
  - `es_actual` (TRUE para registro vigente)
  - `version` (número de versión del cliente)
- **Campos historificados:** Todos los campos descriptivos
- **Justificación:** Permite análisis de evolución del perfil del cliente
- **Ejemplo:** Cliente que cambia de segmento "Bronze" a "Gold"

**SCD tipo 1 y 2 DIM_PRODUCTO (dim_producto):**
- **Campos tipo 1 (sobrescritura):** `descripcion`, `estado`
- **Campos tipo 2 (con historial):** `precio_base`, `categoria`
- **Campos de control:** `fecha_inicio`, `fecha_fin`, `es_actual`, `version`
- **Justificación:** Historial de precios es crítico para análisis de rentabilidad
- **Ejemplo:** Producto que cambia precio de $100 a $120 mantiene ambas versiones


**Documentar el modelo propuesto y justificar las decisiones de diseño.**

### PI 4:  Modelo de Datos de Ventas

![Diagrama ER](/docs/assets/dimensiones_diagrama.png)

Para el desarrollo de la tabla central `fact_ventas`, se opto por un modelo de **Esquema en Estrella** este diseño permite modelar las tablas de dimensiones ya que es facil y posee un alto remdimiento en consultas.

Este modelo permite registrar y analizar las ventas de una empresa a lo largo del tiempo. Está dividido en tablas de **dimensiones** (clientes, productos, fechas, ubicaciones) y una **tabla de hechos** donde se almacena cada venta realizada.

---

## Justificación

Se eligió este modelo para facilitar el análisis histórico de las ventas. La estructura permite hacer preguntas como:

- ¿Qué productos se venden más?
- ¿Quiénes son los mejores clientes?
- ¿En qué lugares hay más ventas?
- ¿Cómo cambian las ventas por mes o por año?

Además, se usan métodos como SCD Tipo 1 y Tipo 2 para guardar cambios en los datos sin perder el historial, por ejemplo si cambia el precio de un producto o la categoría a la que pertenece.

---

## Tabla: `dim_clientes`

Guarda información de los clientes.

- id: identificador interno del cliente (clave primaria).
- cliente_id: ID original del cliente del sistema fuente.
- nombre: nombre completo del cliente.
- email: correo electrónico del cliente.
- fecha_inicio: fecha en la que comienza a ser válida esta versión del cliente.
- fecha_fin: fecha en la que deja de ser válida (por defecto, infinita).
- fecha_creacion: cuándo se insertó el registro.

> Esta tabla guarda historial de cambios (SCD Tipo 2).

---

## Tabla: `dim_productos`

Contiene información de los productos que se venden.

- id: identificador interno del producto.
- producto_id: ID original del producto.
- nombre_producto: nombre del producto.
- descripcion: descripción del producto (sin historial, SCD Tipo 1).
- categoria: categoría del producto (con historial, SCD Tipo 2).
- precio_base: precio base (con historial, SCD Tipo 2).
- estado: estado actual (activo, descontinuado, etc.) (SCD Tipo 1).
- fecha_inicio: fecha en que inicia la validez del registro.
- fecha_fin: fecha en que deja de ser válido.
- fecha_creacion: fecha en la que se creó el registro.

---

## Tabla: `dim_fecha`

Permite hacer análisis por año, mes, día, etc.

- id: identificador de la fecha (clave primaria).
- fecha: fecha completa (tipo DATE).
- año: año de la fecha.
- trimestre: trimestre del año (1 a 4).
- mes: número del mes (1 a 12).
- dia: día del mes.
- dia_semana: día de la semana (1 = lunes, 7 = domingo).

---

## Tabla: `dim_ubicaciones`

Guarda las ubicaciones relacionadas a las ventas (cliente o tienda).

- id: identificador de la ubicación.
- pais: país de la ubicación.
- estado: estado o provincia (opcional).
- ciudad: ciudad.
- codigo_postal: código postal.
- region: región o zona.
- fecha_ultima_actualizacion: cuándo se actualizó por última vez.


---

## Tabla: `fact_ventas`

Registra cada venta realizada. Se conecta con las tablas de dimensiones.

- id: identificador de la venta (clave primaria).
- cliente_id: referencia a un cliente en `dim_clientes`.
- producto_id: referencia a un producto en `dim_productos`.
- fecha_id: referencia a una fecha en `dim_fecha`.
- ubicacion_id: referencia a una ubicación en `dim_ubicaciones`.

---


> **[Ver Avance 3: Implementación DBT y Modelo Físico](../Avance_3/README.md)**


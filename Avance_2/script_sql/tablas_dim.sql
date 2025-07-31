CREATE TABLE dim_clientes (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER NOT NULL,     -- ID original del cliente
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    -- Campos SCD tipo 2
    fecha_inicio DATE NOT NULL DEFAULT CURRENT_DATE,
    fecha_fin DATE DEFAULT '9999-12-31',
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE dim_productos (
    id SERIAL PRIMARY KEY,
    producto_id INTEGER NOT NULL,                -- ID original del producto
    nombre_producto VARCHAR(200) NOT NULL,
    descripcion VARCHAR(255),                    -- campo SCD tipo 1                   
    categoria VARCHAR(50) NOT NULL,              -- campo SCD tipo 2                             
    precio_base DECIMAL(10,2) NOT NULL,          -- campo SCD tipo 2   
    estado VARCHAR(20) NOT NULL,                 -- campo SCD tipo 1   
    -- Campos SCD tipo 2
    fecha_inicio DATE NOT NULL DEFAULT CURRENT_DATE,
    fecha_fin DATE DEFAULT '9999-12-31',
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE dim_fecha (
    id INTEGER PRIMARY KEY,            
    fecha DATE NOT NULL,
    año INTEGER NOT NULL,
    trimestre INTEGER NOT NULL,
    mes INTEGER NOT NULL,
    dia INTEGER NOT NULL,
    dia_semana INTEGER NOT NULL
);


CREATE TABLE dim_ubicaciones (
    id SERIAL PRIMARY KEY,
    pais VARCHAR(50) NOT NULL,
    estado VARCHAR(50),
    ciudad VARCHAR(50) NOT NULL,
    codigo_postal VARCHAR(10),
    region VARCHAR(50),                   
    fecha_ultima_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE fact_ventas (
    id SERIAL PRIMARY KEY,
    -- Claves foráneas hacia dimensiones
    cliente_id INTEGER NOT NULL,
    producto_id INTEGER NOT NULL,
    fecha_id INTEGER NOT NULL,
    ubicacion_id INTEGER NOT NULL,

    cantidad_vendida INTEGER NOT NULL,
    precio_por_unidad DECIMAL(10,2) NOT NULL,
    monto_total DECIMAL(10,2) NOT NULL,
    fecha_carga TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (cliente_id) REFERENCES dim_clientes(id),
    FOREIGN KEY (producto_id) REFERENCES dim_productos(id),
    FOREIGN KEY (fecha_id) REFERENCES dim_fecha(id),
    FOREIGN KEY (ubicacion_id) REFERENCES dim_ubicaciones(id)
);
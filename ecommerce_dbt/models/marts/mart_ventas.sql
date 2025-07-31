{{ config(materialized='table') }}

SELECT 
    o.id_orden,
    o.fecha_orden,
    u.id_usuario,
    u.nombre AS usuario_nombre,
    p.id_producto,
    p.nombre AS producto_nombre,
    c.nombre AS categoria,
    do.cantidad,
    do.precio_unitario,
    do.cantidad * do.precio_unitario AS total_orden
FROM {{ ref('stg_ordenes') }} o
JOIN {{ ref('stg_usuarios') }} u ON o.id_usuario = u.id_usuario
JOIN {{ ref('stg_detalle_ordenes') }} do ON o.id_orden = do.id_orden
JOIN {{ ref('stg_productos') }} p ON do.id_producto = p.id_producto
JOIN {{ ref('stg_categorias') }} c ON p.id_categoria = c.id_categoria

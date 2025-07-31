{{ config(materialized='table') }}

SELECT 
    p.id_producto,
    p.nombre,
    c.nombre AS categoria,
    SUM(do.cantidad) AS total_vendido,
    SUM(do.cantidad * do.precio_unitario) AS ingresos
FROM {{ ref('stg_productos') }} p
JOIN {{ ref('stg_categorias') }} c ON p.id_categoria = c.id_categoria
LEFT JOIN {{ ref('stg_detalle_ordenes') }} do ON p.id_producto = do.id_producto
GROUP BY p.id_producto, p.nombre, c.nombre

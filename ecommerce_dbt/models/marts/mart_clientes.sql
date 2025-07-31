{{ config(materialized='table') }}

SELECT 
    u.id_usuario,
    u.nombre,
    u.email,
    COUNT(o.id_orden) AS total_ordenes,
    SUM(do.cantidad * do.precio_unitario) AS total_gastado
FROM {{ ref('stg_usuarios') }} u
LEFT JOIN {{ ref('stg_ordenes') }} o ON u.id_usuario = o.id_usuario
LEFT JOIN {{ ref('stg_detalle_ordenes') }} do ON o.id_orden = do.id_orden
GROUP BY u.id_usuario, u.nombre, u.email

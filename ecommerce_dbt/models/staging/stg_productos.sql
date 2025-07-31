{{ config(materialized='view') }}

SELECT *
FROM {{ source('ecommerce_pg', 'productos') }}

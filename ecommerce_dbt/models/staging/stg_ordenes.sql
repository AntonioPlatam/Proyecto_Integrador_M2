{{ config(materialized='view') }}

SELECT *
FROM {{ source('ecommerce_pg', 'ordenes') }}

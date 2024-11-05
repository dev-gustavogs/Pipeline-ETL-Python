-- models/staging/stg_movimentacao_commodities.sql

with source as (
    select
        Date,
        Symbol,
        action,
        quantity
    from 
        {{ source("databaseteste_44aj",'movimentacao_commodities') }}
),

renamed as (
    select
     cast(date as date) as data,
        Symbol as simbolo,
        action as acao,
        quantity as quantidade
    from source
)

select * from renamed
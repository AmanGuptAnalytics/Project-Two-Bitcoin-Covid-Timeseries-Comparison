
with source as (

    select * from {{ source('B_C_Raw_Data','Bitcoin_price_raw')}}
)

Select 
    cast(Time as DATETIME) as Date_Time,
    cast(Price as FLOAT64) as Daily_price

    from source 
    where Price is not null
    order by Date_Time DESC 
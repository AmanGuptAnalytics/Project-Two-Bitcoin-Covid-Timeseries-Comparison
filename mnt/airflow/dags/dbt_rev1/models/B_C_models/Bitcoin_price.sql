
with source as (

    select * from {{ source('B_C_Raw_Data','Bitcoin_price_raw')}}
)


Select EXTRACT(date from Date_Time ) as Date, Daily_price 
from
 (

Select 
    cast(Time as DATETIME) as Date_Time,
    cast(Price as FLOAT64) as Daily_price

    from source 
    where Price is not null AND Time is not null 
    order by Date_Time DESC 
)

where Daily_price > 10
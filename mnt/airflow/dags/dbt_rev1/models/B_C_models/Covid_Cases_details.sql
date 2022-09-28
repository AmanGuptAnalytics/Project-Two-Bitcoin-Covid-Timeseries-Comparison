
Select date,  Cases_USA, Cases_China, Cases_Japan, Cases_Germany, Cases_UK, Cases_India, Cases_France, Cases_Canada, Cases_South_Korea
from
(
Select date, sum(USA) as Cases_USA, sum(China) as Cases_China, sum(Japan) as Cases_Japan, sum(Germany) as Cases_Germany,
sum(UK) as Cases_UK, sum(India) as Cases_India, sum(France) as Cases_France, sum(Canada) as Cases_Canada, sum(South_Korea) as Cases_South_Korea
 
from

(SELECT 
    date, 
   
    case when country_name = "United States of America" then sum(new_confirmed) end as USA,
    case when country_name = "China" then sum(new_confirmed) end as China,
    case when country_name = "Japan" then sum(new_confirmed) end as Japan,
    case when country_name = "Germany" then sum(new_confirmed) end as Germany,
    case when country_name = "United Kingdom" then sum(new_confirmed) end as UK,
    case when country_name = "India" then sum(new_confirmed) end as India,
    case when country_name = "France" then sum(new_confirmed) end as France,
    case when country_name = "Italy" then sum(new_confirmed) end as  Italy,
    case when country_name = "Canada" then sum(new_confirmed) end as Canada,
    case when country_name = "South Korea" then sum(new_confirmed) end as South_Korea
      

FROM `bigquery-public-data.covid19_open_data.covid19_open_data` where country_name =  "United States of America" or country_name = "China"
or country_name =  "Japan" or country_name =  "Germany" or country_name =  "United Kingdom" or country_name =  "India"
or country_name =  "France" or country_name =  "Italy" or country_name =  "Canada" or country_name =  "South Korea"
 group by  1,country_name order by 1 desc
 )
 group by 1 order by 1 desc
)
where date is not null AND 
      Cases_USA > 10 AND CASES_USA is not NULL AND
      Cases_China > 10 AND CASES_China is not NULL AND 
      Cases_Japan > 10 AND CASES_Japan is not NULL AND
      Cases_Germany > 10 AND CASES_Germany is not NULL AND
      Cases_UK > 10 AND CASES_UK is not NULL AND
      Cases_India > 10 AND CASES_India is not NULL AND
      Cases_France > 10 AND CASES_France is not NULL AND
      Cases_Canada > 10 AND CASES_Canada is not NULL AND
      Cases_South_Korea > 10 AND CASES_South_Korea is not NULL 



Select date, sum(USA) as USA, sum(China) as China, sum(Japan) as Japan, sum(Germany) as Germany,
sum(UK) as UK, sum(India) as India, sum(France) as France, sum(Canada) as Canada, sum(South_Korea) as South_Korea
 
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
 group by  1,country_name order by 1 desc)

 group by 1 order by 1 desc
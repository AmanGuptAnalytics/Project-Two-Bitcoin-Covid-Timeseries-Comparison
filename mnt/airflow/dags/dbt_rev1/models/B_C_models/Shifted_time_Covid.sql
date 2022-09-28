SELECT  (cc.date - 7 ) as date , 
        (cc.Cases_USA + cc.Cases_China + cc.Cases_Japan + cc.Cases_Germany + 
        cc.Cases_UK + cc.Cases_France + cc.Cases_India+cc.Cases_Canada + cc.Cases_South_Korea
        ) as Top_Nine_Economies, btc.Date as Btc_Date, btc.Daily_price
        
FROM `bitcoin-and-covid-comparison.B_C_model_bitcoin_dataset_bitcoin_dataset.Covid_Cases_details` cc ,
`bitcoin-and-covid-comparison.B_C_model_bitcoin_dataset_bitcoin_dataset.Bitcoin_price` btc 

where cc.date = btc.Date
order by 1 desc,3 desc

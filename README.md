# Tadawul
tadawul parsing and scraping <br />
Done by **Abdullah omran** , <br />

## Main file
the main file is Tadawul_Parser.py <br />
and until now there are 4 available functions : <br />

## stockscreaper(Stock Code , Period ) 
scrape daily price of stock based on stock code<br />
ex. stockscreaper(stock code <2030>, num for 30 days <1> for 30 days or <2> for 60 days ...)<br />

## TASI(Period) 
scrape the main index of Saudi Market , ex. TASI(1) will scrape index of 10 days, TASI(3) index of 30 day . <br />

## TASI(StartDate, EndDate, Period) 
This fun. becuase the previeus set for fixed date , while this will start from EndDate for Period*10 <br />
or until it reach StartDate .  <br />


## divdscraper(Stock Code) 
scrape all past dividend of stock based on the code of stock <br />
ex. divdscraper(Code of stock for ex. <2030>)<br />

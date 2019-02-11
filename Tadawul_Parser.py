#####This script done by abdullah omran to scrape tadawul stock market dividend , as they dont offer any api services . 
##Not responisble for any voliation of laws , 

## this script have 3 finctions : 
## 1-stockscreaper : scrape daily price of stock based on stock code ex. stockscreaper(stock code <2030>, num for 30 days <1> for 30 days or <2> for 60 days ...
## 2-divdscraper : scrape dividend of stock 
## 3-TASI : scrape the main index of Saudi Market , ex. TASI(1) will scrape index of 10 days . TASI(3) index of 30 day . 


from Stock import stockscreaper
from Divid import divdscraper
from TASI import TASI


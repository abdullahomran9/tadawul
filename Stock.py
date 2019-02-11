

###This script done by abdullah omran to scrape tadawul stock market prices , as they dont offer any api services . 
##Not responisble for any voliation of laws , 

##to use , recall stockscrapper fun , like this : 
##stockscreaper(Code of stock for ex. <2030> , days scraping * 30 for ex. <3> mean 90 days )


import urllib.request
import urllib.parse
import json
import time
import os
import sys
import codecs



def stockscreaper(code,period):
    stockCode=code
    filename=str(code)+str(".csv")
    z=period
    file = codecs.open("Price-"+str(filename), "a", "utf-8")
    print(stockCode)
    print(filename)
    print(z)
    
    for x in range (z):

        z="2012-02-03&toDate=2019-01-21"   ## period of scrapping
        stockCode="2030" ## code of stock
        part5=('&symbol='+str(stockCode)+'&_=1548113462455')
        part4=str(z)
        part3=('&length=30&search%5Bvalue%5D=&search%5Bregex%5D=false&isNonAdjusted=0&startDate=')
        part2=str(x*30)
        part1=('https://www.tadawul.com.sa/wps/portal/tadawul/market-participants/issuers/issuers-directory/company-details/!ut/p/z1/pZDJjoJAFEW_xQXruhagtDsEBARJI-JQG1NOSMK0oLujX285bEwU2_h2LznnvrxLGJkTVvDfNOF1WhY8E_uCdZaB4xsONOrZ1kSG3jFHxjhwKQAyuwCUGlr7S4EPv9sWgA03HCkyQpmwt3zbDbrQQ92ZDqYC1ehnPpT_-XgyOl75Q8KSrFxdq9rXddWTIKHmG_73k0lCX5d5xYtDdMhXpYAo5PNRdp8Lh5oi1_I801Ap-uoNaOr1HnhQXCNwbuYCNLwebQtS5XEcz4_-LnLT76TVOgFmv1Hm/p0/IZ7_NHLCH082KGET30A6DMCRNI2086=CZ6_NHLCH082KGET30A6DMCRNI2000=NJhistoricalPerformance=/?draw=2&columns%5B0%5D%5Bdata%5D=transactionDateStr&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=todaysOpen&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=highPrice&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=lowPrice&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=previousClosePrice&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=change&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=changePercent&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=volumeTraded&columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=turnOver&columns%5B8%5D%5Bname%5D=&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=noOfTrades&columns%5B9%5D%5Bname%5D=&columns%5B9%5D%5Bsearchable%5D=true&columns%5B9%5D%5Borderable%5D=true&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&start=')
        url=(part1+part2+part3+part4+part5)
        ##print(url)


        req=urllib.request.Request(url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )
        resp=urllib.request.urlopen(req)
        respData=resp.read()
        strData=str(respData)
        splitData=strData.replace('{','')
        replData=splitData.replace('},','\n')
        removData,unwan,tail=replData.partition('"data":[')
        aa,bb,cc=tail.partition('],"recordsTo')
        removeunwanted1=aa.replace('"transactionDate":','')
        removeunwanted2=removeunwanted1.replace('"transactionDateStr":','').replace('"previousClosePrice":','').replace('"todaysOpen":','').replace('"turnOver":','')
        removeunwanted3=removeunwanted2.replace('"turnOver":','').replace('"noOfTrades":','').replace('"volumeTraded":','').replace('"lowPrice":','')
        removeunwanted4=removeunwanted3.replace('"change":','').replace('"highPrice":','').replace('"changePercent":','').replace('"lastTradePrice":','')
        removeunwanted5=removeunwanted4.replace('"','').replace('}','').replace(', ',' ')
        print("Vlaues scraped= "+str((x+1)*30)+" , X="+str(x+1))

        file.write("\n"+removeunwanted5)
        time.sleep(2)
    file.close()
    

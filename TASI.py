
##to use , recall TASI fun , like this : 
##TASI(insert an integer , note that the scraped days will = num *10 , ex. TASI(3) will scrape 30 days )
## if you want to edit the starting and finishing date var part4



import urllib.request
import urllib.parse
import json
import time
import os
import sys
import codecs



def TASI(period):
    #Sdat=StartDate
    #Sdat=dat.replace('/','%2F')
    #Edat=EndDate
    #Edat=Edat.replace('/','%2F')
    filename=str("TASI")+str(".csv")
    z=period
    file = codecs.open(filename, "a", "utf-8")
    for x in range (z):


        part5=('&typeOfCall=adjustedType&_=1548501991458')
        part4=str('2010%2F03%2F14+-+2019%2F01%2F21')
        part3=('&length=10&search%5Bvalue%5D=&search%5Bregex%5D=false&sourceCallerId=datePicker&dateParameter=')
        part2=str(x*10)
        part1=('https://www.tadawul.com.sa/wps/portal/tadawul/markets/equities/indices/today/!ut/p/z1/rZJdT8IwFIZ_TS-lZ4CA3jUa5swkEr5mb5auHMZM1y5t-fDfu2FiQoJTo71rz_P0zTkt5TShXIt9kQtfGC1UvX_hg7TbvRsFN32IIR4GwAYhRNOnfi8cA121ARAGlP_KD6PJENiUPSzHy3nt9_7mQ_9nPnyxGHzv81ZkErQDpxGdAxdm0Ao0TZ6Ali4eKc-VyT5elOmsN8opt7hBi7azs_Xx1vvK3RIgcDgcOrkxucKONCWBS8rWOE-Tc5LOUDdB7QOrL2uiPpOKrPyIOZZKOwKVNWsCa-GFf6uQgDTao_YELDqzsxKvpFEKZfNBHeVeZJFe45Emz2g3xpZCS_zvELkV1qdeuCKVO2trMnV10ViazNksolW5WCwSKKLXa7WPN_cxrtg7Mrs6jg!!/p0/IZ7_NHLCH082KGN530A68FC4AN2OM2=CZ6_22C81940L0L710A6G0IQM43GF0=N/?draw=5&columns%5B0%5D%5Bdata%5D=date&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=open&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=high&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=low&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=close&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=totalVolume&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=totalTurnover&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=noOfTrades&columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&start=')
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
        removeunwanted5=removeunwanted4.replace('}','').replace(':',',').replace(', ',' ')
        print("Vlaues scraped= "+str((x+1)*10)+" , X="+str(x+1))
        
        file.write("\n"+removeunwanted5)
        time.sleep(2)
    
    #print(removeunwanted5)  
    file.close()
    
    
    
def TASI2(StartDate,EndDate,period):
    Sdat=StartDate
    Sdat=Sdat.replace('/','%2F')
    Edat=EndDate
    Edat=Edat.replace('/','%2F')
    filename=str("TASI2")+str(".csv")
    z=period
    file = codecs.open(filename, "a", "utf-8")
    for x in range (z):


        part5=('&typeOfCall=adjustedType&_=1548501991458')
        part4=(str(Sdat)+'+-+'+str(Edat))
        part3=('&length=10&search%5Bvalue%5D=&search%5Bregex%5D=false&sourceCallerId=datePicker&dateParameter=')
        part2=str(x*10)
        part1=('https://www.tadawul.com.sa/wps/portal/tadawul/markets/equities/indices/today/!ut/p/z1/rZJdT8IwFIZ_TS-lZ4CA3jUa5swkEr5mb5auHMZM1y5t-fDfu2FiQoJTo71rz_P0zTkt5TShXIt9kQtfGC1UvX_hg7TbvRsFN32IIR4GwAYhRNOnfi8cA121ARAGlP_KD6PJENiUPSzHy3nt9_7mQ_9nPnyxGHzv81ZkErQDpxGdAxdm0Ao0TZ6Ali4eKc-VyT5elOmsN8opt7hBi7azs_Xx1vvK3RIgcDgcOrkxucKONCWBS8rWOE-Tc5LOUDdB7QOrL2uiPpOKrPyIOZZKOwKVNWsCa-GFf6uQgDTao_YELDqzsxKvpFEKZfNBHeVeZJFe45Emz2g3xpZCS_zvELkV1qdeuCKVO2trMnV10ViazNksolW5WCwSKKLXa7WPN_cxrtg7Mrs6jg!!/p0/IZ7_NHLCH082KGN530A68FC4AN2OM2=CZ6_22C81940L0L710A6G0IQM43GF0=N/?draw=5&columns%5B0%5D%5Bdata%5D=date&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=open&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=high&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=low&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=close&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=totalVolume&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=totalTurnover&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=noOfTrades&columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&start=')
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
        removeunwanted5=removeunwanted4.replace('}','').replace(':',',').replace(', ',' ')
        print("Vlaues scraped= "+str((x+1)*10)+" , X="+str(x+1))
        
        file.write("\n"+removeunwanted5)
        #print(removeunwanted5)
        time.sleep(2)
    
    #print(removeunwanted5)  
    file.close()

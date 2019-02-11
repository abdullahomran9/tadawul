


###This script done by abdullah omran to scrape tadawul stock market dividend , as they dont offer any api services . 
##Not responisble for any voliation of laws , 

##to use , recall divdscraper fun , like this : 
##divdscraper(Code of stock for ex. <2030>)



import urllib.request
import urllib.parse
from lxml import etree
import codecs
import os 


def divdscraper (code):
    codeStock=code
    url=('https://www.tadawul.com.sa/wps/portal/tadawul/market-participants/issuers/issuers-directory/company-details/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zi_Tx8nD0MLIy83V1DjA0czVx8nYP8PI0MDAz0I4EKzBEKDEJDLYEKjJ0DA11MjQzcTfXDCSkoyE7zBAC-SKhH/?companySymbol='+str(codeStock))
    req=urllib.request.Request(url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )
    resp=urllib.request.urlopen(req)
    respData=resp.read()
    parser = etree.HTMLParser()
    tree = etree.fromstring(respData, parser)
    el3=''
    el2=''
    el=''
    file = codecs.open("div-"+str(codeStock)+".csv", "a", "utf-8")

    for x in range(100):
        Divx=('//*[@id="dividendsTable"]/tbody/tr['+str(x)+']//text()')


        for el in tree.xpath(Divx):


            el=el.strip().replace('/','-').replace('\n',' ').replace('\t',' ').replace('\r',' ')
            ##filter(str.strip,el2)
            #print(el2)
            el3+=str(el)
            if el:
                el3+=str(',')
        if el3:
            el3+=str("\n")
    el3 = os.linesep.join([s for s in el3.splitlines() if s])    
    print(el3)
    file.write("\n"+el3)
    file.close()
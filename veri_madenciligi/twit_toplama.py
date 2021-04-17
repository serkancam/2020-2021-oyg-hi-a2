from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from bs4 import BeautifulSoup
import os
import pandas as pd
import time

tarayici_yolu = os.path.join(os.getcwd(),"veri_madenciligi","geckodriver.exe")
ayarlar = FirefoxOptions()
# ayarlar.add_argument("--headless")
surucu = webdriver.Firefox(options=ayarlar,executable_path=tarayici_yolu)
surucu.get(url="https://twitter.com/edirnebilsem")
time.sleep(10)
icerik=surucu.page_source
# print(icerik)
soup = BeautifulSoup(icerik,"hmtl.parser")
# print(soup)
dosya=open("twitler.txt",mode="w+",encoding="utf-8")
for a in soup.find_all("div",attrs={"data-testid":"tweet"}):      
    twit = a.find("span",attrs={"class":"css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"})
    dosya.write(twit.text)
dosya.close()
   
    
    
   
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from bs4 import BeautifulSoup
import os
import pandas as pd
import time

# yol = os.path.join(os.getcwd(), "veri_madenciligi", "geckodriver.exe")
# dosya_yolu=os.path.join(os.getcwd(), "veri_madenciligi", "dmo.csv")
# options = FirefoxOptions()
# options.add_argument("--headless") 
# driver = webdriver.Firefox(options=options, executable_path=yol)
# driver.get("https://www.dmo.gov.tr/Arama?s=&k=%7c%7cElektronik%7c%7cBilgisayarlar%7c%7cDiz%c3%bcst%c3%bc+Bilgisayarlar&p=1&d=SM&e=1")
# content = driver.page_source
# soup = BeautifulSoup(content, "lxml")
# urun = []  
# marka = []  
# fiyat = []  
# id = []
# adres = []
# islemci=[]
# ram=[]
# ekran=[]
# depolama=[]


# for a in soup.find_all('div', attrs={'class': 'product-item'}):
#     try:
#         adi = a.find('div', attrs={'class': 'title'})
#         # marka=a.find('div', attrs={'class':'brand'})
#         para = a.find('span', attrs={'class': 'price-current text-center'})

#         if para and adi :
#             fiyat.append(para.text.split(" ")[0])
#             urun.append(adi.find("a").text)
#             adres.append(adi.find("a").get("href"))
#             # print(para.text.split(" ")[0])
#     except :
#         print("hata")
# i=0
# for href in adres:
#     try:
#         i+=1
#         print(f"{i}. ürün yazdırılıyor.")
#         driver.get("https://www.dmo.gov.tr"+href)
#         driver.find_element_by_xpath('//*[@id="tanimTab"]/a').click() 
#         time.sleep(1)

#         islemci.append(driver.find_element_by_xpath('//*[text()="İşlemci Modeli Serisi:"]/ancestor::div/following-sibling::div').text)
#         ram.append(driver.find_element_by_xpath('//*[text()="Bellek Kapasitesi:"]/ancestor::div/following-sibling::div').text)
#         ekran.append(driver.find_element_by_xpath('//*[text()="Ekran Boyutu (inch):"]/ancestor::div/following-sibling::div').text)
#         depolama.append(driver.find_element_by_xpath('//*[text()="Harddisk Tipi:"]/ancestor::div/following-sibling::div').text)
              
#         # islemci.append(driver.find_element_by_xpath('//*[@id="tanim"]/ul[3]/li[4]/div[2]').text)
#         # ram.append(driver.find_element_by_xpath('//*[@id="tanim"]/ul[3]/li[17]/div[2]').text)
#         # ekran.append(driver.find_element_by_xpath('//*[@id="tanim"]/ul[4]/li[2]/div[2]').text)
#         # depolama.append(driver.find_element_by_xpath('//*[@id="tanim"]/ul[3]/li[7]/div[2]').text)
#         # print(islemci[-1],ram[-1],ekran[-1],depolama[-1])

#     except :
#         print("sayfa ayrıntı hatası:")

    
# veri = {"Urun":urun,"adres":adres,"fiyat":fiyat,"işlemci":islemci,"ram":ram,"ekran":ekran,"depolama":depolama}
# veri = pd.DataFrame(veri)
# veri.to_csv(dosya_yolu)
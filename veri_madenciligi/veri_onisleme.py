#veri_onisleme.py
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %% dosyayı içe ataralım
veri = pd.read_csv("kalp_rahatsizligi.csv")
veri.head()

# %% sütun isimlerinin değiştirilmesi
veri.info()
veri.columns
#%%
#serum_kolestrol -->kolestrol
#gogus_agrisi_tipi-->gat
#hareketsiz_kan_basincini-->hkb 
veri.rename(columns={
    'yas':'yas', 
    'cinsiyet':"cinsiyet",
    'gogus_agrisi_tipi':"gat", 'hareketsiz_kan_basinci':"hkb",
    'serum_kolestrol':"kolestrol",
    'aclik_kan_sekeri':"aks",
    'elektrokardiyografi':"ekg",
    'en_yuksek_kalp_hizi':"eykh", 'anjin_bagli_egsersiz':"abe",
     'st_depresyonu':"st_d",
    'st_egimi':"st_e", 
    'buyuk_damarlar':"bds",
     'talasemi':"talasemi", 
     'kalp_rahatsizligi':"rahatsizlik"},inplace=True)



# %% bir sütunun veya sütunların kaldırılması
veri.head(3)
veri2=veri.drop(["yas","cinsiyet"],axis=1)

# %% kayıp verilerin işlenmesi
# sklearn sürekli np.ndarray veri tipi ile çalışır
from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values=np.nan,strategy="most_frequent")

bds=veri["bds"].values.reshape(-1,1)
sonuc=imp.fit_transform(bds)
veri["bds"]=sonuc
veri.info()
# print(bds)
#%%


# %%
veri.info()

# %% kayıp veri içeren satırları silmek

veri.dropna(axis=0,inplace=True)
veri.info()

# %%

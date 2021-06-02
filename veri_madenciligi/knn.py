#%% kütüphaneler
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# %%
veri = pd.read_csv("kalp_rahatsizligi.csv")
# %%
veri.rename(columns={
    "gogus_agrisi_tipi":"gat",
    "hareketsiz_kan_basinci":"hkb",
    "serum_kolestrol":"sk",
    "aclik_kan_sekeri":"aks",
    "elektrokardiyografi":"ekg",
    "en_yuksek_kalp_hizi":"eykh",
    "anjin_bagli_egsersiz":"abe",
    "st_depresyonu":"st_d",
    "st_egimi":"st_e",
    "buyuk_damarlar":"bds"},inplace=True)
# %%
# 1- eksik veriler giderilecek
# 2- aykırı verile giderilebilşir(opsiyonel) 
# 3- kategorik verileri sayısal değerler ile ifade etmek
# 3.1- verileri öznitelikler ve sınıf gibi iki bölüme ayırdım 
# 4- sayısal verileri 0-1 arasına normalize etmek
# 5- veri setinin son halini eğitim verisi/test veirisi oalrak bölmek

#%% 1- eksik verilerin giderilmesi.
from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan,strategy="most_frequent")
bds=veri["bds"].values.reshape(-1,1)
tal=veri["talasemi"].values.reshape(-1,1)
veri["bds"]=imputer.fit_transform(bds)
veri["talasemi"]=imputer.fit_transform(tal)
#%% kategorik verilerin etiketlenmesi
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
veri["cinsiyet"]=le.fit_transform(veri["cinsiyet"])
#%%
veri["gat"]=le.fit_transform(veri["gat"])
veri["ekg"]=le.fit_transform(veri["ekg"])
veri["st_e"]=le.fit_transform(veri["st_e"])
veri["talasemi"]=le.fit_transform(veri["talasemi"])
# %% 4- yas,hkb ,sk,eykh,st_d,bds(0,3,4,7,9,11) sütunları normalize edilecek
from sklearn.preprocessing import minmax_scale

y=veri.iloc[:,13].values
x_data=veri.iloc[:,0:-1].values

#%%
x_data[:,[0,3,4,7,9,11]]=minmax_scale(x_data[:,[0,3,4,7,9,11]],feature_range=(0,1))

# %% elimizdeki veri setini train(eğitim) ve test kısmı olarak parçalıyourz.
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x_data,y,test_size=0.2,random_state=22)


# %% en yakın komuşu modelinin oluşturulması
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train,y_train)
# %% test ediyorum
tahmin=knn.predict(x_test)
for i in range(len(tahmin)):
    print(f"gerçek değer:{y_test[i]}--tahmin edilen:{tahmin[i]}\n")

# %%
ogrenme_skoru=knn.score(x_test,y_test)
print(f"Öğrenme skoru:{ogrenme_skoru}")

# %%

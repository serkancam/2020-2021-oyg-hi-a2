#%%
import pandas as pd
sozluk = {"isim":["eren","reyyan","mert","atahan","serkan"],
        "yas":[13,13,12,15,39],
        "boy":[1.56,1.58,1.65,1.76,1.74],
        "kilo":[50,45,53,60,78]
        }
veri = pd.DataFrame(sozluk,index={1,2,3,4,5})
veri

# %%
veri.head(3)
# %%
veri.tail(2)
# %%
veri.columns
# %%
veri.info()
# %%
veri = pd.read_csv("kalp_rahatsizligi.csv")
veri.head()
# %%
print(veri.columns)

# %%
veri.info()
# %%
veri.describe()
# %%
veri["serum_kolestrol"]
# %% filtreleme
veri[veri["yas"]>50]
# %%
veri[veri.hareketsiz_kan_basinci>120]
# %%
ort = veri["serum_kolestrol"].mean()
std =veri["serum_kolestrol"].std()
print("serum_koelstrol ortalaması=",ort)
print("serum_koelstrol standart sapma=",std)


# %% yaşı 50 den büyük kadınların serum_kolestrol ortalaması
import pandas as pd
veri = pd.read_csv("kalp_rahatsizligi.csv")
kadin_veri=veri[(veri.cinsiyet=="kadin")&(veri.yas>50)]
kadin_veri["serum_kolestrol"].mean()

# %%

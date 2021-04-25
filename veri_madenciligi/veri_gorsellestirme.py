#%%
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

veri = pd.read_csv("kalp_rahatsizligi.csv")
veri.info()
# %% histogram grafiği, gruplandırılmış verilerin dağılımı hakkında bilgi verir.
#%% yaş verisi histogram
sns.histplot(data=veri,x="yas",bins=10)
plt.xlabel("Yaş")
plt.ylabel("Adet")
plt.show()


# %% cinsiyete göre yaş dağılım histogramı
sns.histplot(data=veri,x="yas",hue="cinsiyet",element="step")
plt.xlabel("Yaş")
plt.ylabel("Adet")
plt.show()

# %% gogus agrisi histogram
sns.histplot(data=veri,x="gogus_agrisi_tipi",hue="cinsiyet",element="bars")
plt.show()


# %%
sns.displot(data=veri,x="gogus_agrisi_tipi",hue="cinsiyet")
plt.show()
# %% kolestrol değerinin dağılımını cinsiyete göre histogram grafiğini çizdiriniz. bins değeride 20 olsun
sns.histplot(x="serum_kolestrol",data=veri,bins=20,hue="cinsiyet",element="step")
plt.show()

# %% Saçılım garfiği:(scatterplot)

#%%hareketsiz kan basıncı - en yüksek kal hızı saçılım grafiği cinsiyete göre gruplu
sns.scatterplot(x="en_yuksek_kalp_hizi",y="hareketsiz_kan_basinci",hue="cinsiyet",data=veri)
plt.show()
#%%
sns.scatterplot(x="en_yuksek_kalp_hizi",y="hareketsiz_kan_basinci",hue="kalp_rahatsizligi",data=veri)
plt.show()
# %% serum_kolestol ile yas verileri araındaki saçılım grafiğini gogus_agrisi_tipi	ile gruplayarak göre çizdiriniz
sns.scatterplot(x="serum_kolestrol",y="yas",data=veri,hue="gogus_agrisi_tipi")
plt.show()
# %% serum_kolestol ile yas verileri araındaki saçılım grafiğini kalp_rahatsizligi	ile gruplayarak göre çizdiriniz
sns.scatterplot(x="serum_kolestrol",y="yas",data=veri,hue="kalp_rahatsizligi")
plt.show()
# %% çigi grafiği belli bir değerin zamana bağlı olarak değimini veya belli bir değere bağlı olarka değişimini ifade etmek için kullanılır.

#%% yaş/serum_kolestrol grafiği

sns.lineplot(data=veri,x="yas",y="serum_kolestrol")
plt.title("Yaş kolestrol grafiği")
plt.show()
#%% yaş/serum_kolestrol grafiği cinsiyet

sns.lineplot(data=veri,x="yas",y="serum_kolestrol",hue="cinsiyet")
plt.title("Yaş kolestrol grafiği")
plt.show()

# %% yas/e yüksek kalp hızı
sns.lineplot(data=veri,x="yas",y="en_yuksek_kalp_hizi")
plt.title("Yaş-En yüksek kalp hızı")
plt.show()

# %%
sns.scatterplot(data=veri,x="yas",y="en_yuksek_kalp_hizi")
plt.title("Yaş-En yüksek kalp hızı")
plt.show()
# %% sütun/çubuk grafiği
# kategrik verilerin toplamları/ortalamarı gibi değerleri ifade etmeye yarar

sns.countplot(x="cinsiyet",data=veri)

plt.show()

# %% talesemi tiplerinin sayısı cinsiyete göre
sns.countplot(x="talasemi",data=veri,hue="cinsiyet",)
plt.show()

# %% # %% talesemi tiplerinin sayısı cinsiyete göre ve kalp rahatsızlığı durumuna göre
sns.catplot(x="kalp_rahatsizligi", hue="elektrokardiyografi", col="talasemi",data=veri, kind="count",height=4, aspect=0.7)
plt.show()
# %% kutu grafiği(box plot)

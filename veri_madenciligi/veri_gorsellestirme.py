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
# sayısal verilerin temel istatistik bilgisini görselleşitmek iin kullanılan grafik türüdür.

# serum kolestrol değerinin kutu grafiği
sns.boxplot(data=veri,y="serum_kolestrol",orient="h")
plt.show()

print(veri["serum_kolestrol"].median())
print(veri["serum_kolestrol"].min())
print(veri["serum_kolestrol"].max())
# %% harketsiz kan basıncı kutu grafiği
sns.boxplot(data=veri,y="hareketsiz_kan_basinci")
plt.show()
print(veri["hareketsiz_kan_basinci"].median())
# %%
sns.boxplot(data=veri,y="yas")
plt.show()

# %% en yüksek kalp hızı
sns.boxplot(data=veri,y="en_yuksek_kalp_hizi")
plt.show()

# %%
# serum kolestrol değerinin kutu grafiği
sns.boxplot(data=veri,y="serum_kolestrol",x="cinsiyet")
plt.show()
# %% serum kolestrol verisin IQR değerini bulalım
#
sk_q1=veri["serum_kolestrol"].describe()[4]
sk_q3=veri["serum_kolestrol"].describe()[6]
sk_IQR=sk_q3-sk_q1
print("serum_kolestrol IQR=",sk_IQR)
# %% hareketsiz kan basıncının kadınlar için ve erkekler için ayrı ayrı kutu grafiğini çizdirerek yine kadın ve erkekler için IQR değerlerini hesaplayınız

sns.boxplot(data=veri,x="cinsiyet",y="hareketsiz_kan_basinci")
plt.show()

# %%
veri_kadin=veri[veri.cinsiyet=="kadin"]
veri_erkek=veri[veri.cinsiyet=="erkek"]
veri_kadin
veri_erkek
kadin_hkn_q3=veri_kadin["serum_kolestrol"].describe()[6]
kadin_hkn_q1=veri_kadin["serum_kolestrol"].describe()[4]
kadin_hkb_iqr=kadin_hkn_q3-kadin_hkn_q1
print("kadın IQR=",kadin_hkb_iqr)
print("kadın Alt sınır",kadin_hkn_q1-1.5*kadin_hkb_iqr)

print("kadın üst sınır",kadin_hkn_q3+1.5*kadin_hkb_iqr)
# %% 
sns.boxplot(data=veri,y="serum_kolestrol",x="cinsiyet",hue="kalp_rahatsizligi")
plt.show()
# %%
g=sns.PairGrid(veri)
g.map(sns.scatterplot())


# %% ısı haritasi grafiği
sns.heatmap(data=veri.corr(),annot=True,linewidths=0.5,fmt="0.1f")
plt.show()

# %%

# %% listeler
l1 = []  # boş liste **
l2 = list()  # boş liste

ogler = ["ahmet efe", "zeynep", "reyyan", "yusuf", "mert",
         "kerem", "tarık"]
mix = [1, 2, 32.0, "hasan", True, True, False]

print(ogler)
print(mix)
print(ogler[1])
ogler[3] = "yusuf aras"
print(ogler)

for isim in ogler:
    print(isim)


# %%
#karakter dizisi koleksiyon
#mutable--değişebilir immutable değişemez

isim ="reyyan/tarık"

for harf in isim:
    print(harf)

print("3. eleman",isim[3])

#isim[3]="h" #immutable

isim="fatih"


# %% in komutu

kelime="merhaba"

sonuc = "er" in kelime
print(sonuc)

# %%
#indis numrası olan tüm koleksiyonlarda
#string list
#tuple
print(kelime)
print(kelime[0:2])#ilk iki
print(kelime[0:4])
print(kelime[-1])# son eleman
print(kelime[3:])#3. elemandan sona kadar
print(kelime[:3])#baştan 3 karakter
print(kelime[3:len(kelime)])
print(kelime[-3:-1])
print(kelime[::2])#baştan iki atlayarak
print(kelime[::-1])#tesrten birer birer

# %%  ilkel tip (primitive)
#ilkel tipler değer tutar ve değer aktarır

sayi1=30
sayi2=sayi1

print("sayi1=",sayi1,"sayi2=",sayi2)
sayi1=25
print("sayi1=",sayi1,"sayi2=",sayi2)
# %% referans tipler
#referans tipler adres  aktarır.


nums=[1,2,3,4]
sayilar=nums#nums[:] bu kullanım sadece değerleri aktarır
print("nums=",nums,"sayilar=",sayilar,sep="\n")

nums[3]=18
print("nums=",nums,"sayilar=",sayilar,sep="\n")
# %% liste fonskiyonları

import random

notlar=[]

for _ in range(5):
    notlar.append(random.randint(50,100))

print(notlar)
isimler=["arda","ahmet","zeynep","reyyan","mert","serkan"]
print(isimler)
print(isimler.count("arda"))
isimler.remove("serkan")
print(isimler)


# %%
import random
import matplotlib.pyplot as plt
notlar=[]

for _ in range(5):
    notlar.append(random.randint(50,100))
isimler=["arda","ahmet","zeynep","reyyan","mert"]

plt.xlabel("isimler")
plt.bar(isimler,notlar)
plt.show()

# %% 

isimler=["arda","ahmet","zeynep","reyyan","mert",
"serkan","arda"]
# print(isimler)
print(isimler.count("arda"))
print(isimler[2])
isimler.remove("zeynep")
print(isimler[2])
print(isimler)

# %% tuple - demet
#immutable değişmez

#t1=tuple() mantıklı değil

kirmizi=(255,0,0)
gri1=(100,105,100)

sari=0,255,255
print(hex(id(sari)))
print(sari[2])
# sari[2]=200
print(hex(id(sari)))


sari=0,255,255
print(hex(id(sari)))

sinavAgirliklari=0.3,0.3,0.4
s1=[50.0,70.0,80.0]

print(gri1.index(105))
print(gri1.count(100))






# %% set-küme

k1={1,2,3,3,1,2,3,2,1,1}
print(id(k1))
print(k1)
k1.add(8)
print(k1)
# print(k1[0])
print(len(k1))

k2={3,8,2,7,12,25}

print(k1.intersection(k2))
print(k1.union(k2))
k1={1,2,3}
print(id(k1))

l1=[1,2,3,5,45]
print(l1.index(5))
# %%
k2={3,8,2,7,12,25}
k1={3,8,7}
print(k1.issubset(k2))

# %% dictionary-sözlük
# mutable değiştirilebilir
# indis yok onun yerine anahtarlar var
# anahtar-değer(key-value) çiftleri tutar

s1 = {2:"ahmet efe",3:"irem",4:"kerem halil",1025:"mert",
"mt":"mehmet tarık",300.5:"reyyan"}

print(s1[4])
print(s1[300.5])
print(s1["mt"])

sonuc = s1.values()
print("kerem halil" in s1.values())

renkler = {"kirmizi":(255,0,0),"mavi":(0,0,255)}
print(renkler)
print(renkler.keys())
print(renkler.values())

renkler["sari"]=(0,255,255)


print("255 var mı:",255 in renkler["kirmizi"])

print(renkler.items())



# %% karışık koleksiyon
# print(renkler.items())
renkler = {"kirmizi":(255,222,0),"mavi":(122,0,255)}
for k,v in renkler.items():
    # print(k,":",v)
    if 122 in v:
        print(k)



# %% karşık koleksiyon
sinavlar = {"ali":[100,80,50],"veli":[75,80,95],
"ayşe":[90,95,[100,95]]}

ayse_32=sinavlar["ayşe"][2][1]
print(ayse_32)
# %% silme

s=5

print(s)
del s
# print(s)

l1=[25,36,36,28,27]
del l1[0]
print(l1)

# %%

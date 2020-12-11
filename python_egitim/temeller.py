#%%
print("merhaba")
isim="Adnan"
yas=20
boy=1.74
print("merhaba",isim,"kaç yaşındasın?",sep=" ",end="\n") #\n yeni satır enter
print("merhaba",yas,"yaşındayım",boy,"metre boyundayım",end="\n")

# %%
r1="sarı"
r2="kırmızı"
print(r1,r2)
# rt=r1
# r1=r2
# r2=rt
r1,r2=r2,r1
print(r1,r2)
f1=1
f2=1
f1,f2=f2,f1+f2
print(f1,f2)
f1,f2=f2,f1+f2
print(f1,f2)
f1,f2=f2,f1+f2
print(f1,f2)
s1=1
s2=1
s3=1
s1,s2,s3=s2,s3,s1+s2+s3
print(s1,s2,s3,sep="-",end="@")
# %% Tip dönüşümler
yas=30.0

print(type(yas))

s1=3/3
print(s1,type(s1))
if type(yas)==type(s1):
    print("aynı")
else:
    print("farklı")

# %% operatörler (işleçler)
s1=38
s2=40.0
s3=s1+s2
print(s3)

bolunen=10
bolen=3.0
bolum=bolunen  // bolen
kalan=bolunen % bolen
print(bolunen,"in",bolen,"e bölümünden bolum=",bolum,"kalan=",kalan)


# %% tip dönüşümleri int,str,float
#int(deger),float(deger),str(deger)
print(int())
print(float())

a=int("30")
b=float("50")
c=a+b
print(c)
isim="veli"
yas=40

mesaj=(str(isim)+" "+str(yas))
print(mesaj)
# %% bool tipler

evliMi=True
print(evliMi)

test1=""
test2=0
test3=0.0
print(bool(test1))
print(bool(test2))
print(bool(test3))

print(int(True))
print(float(True))
print(len("hasan"))
print(len(str(False)))
# print(len(20)) hata

listem=[0,25,36,25]
print(len(listem))
print(10*"-")
sayi="    -30_000.0      "
print(int(sayi))
print(float(sayi))
#%% karşılaştırma operatörleri

s1=10
s2=30
s3=15
print(type(s1 > s2))

print(s1<s3<s2<35)

sonuc = s1 == s2
print(sonuc)

print(s1>=s2)
print(s1<=s2)
print(s1!=s2)

s1=48
s2="kırmızı"
s3="edirne"

sonuc=int(s1==48)+int(s2=="kırmızı")+int(s3=="edirne")
print("sonuç=",sonuc*5)


# %%  kaydırma operatörleri

s1 = 56
print(s1<<2)

s2=33
print(s2>>1)

print(s1,s2)
s1=s2

# %%

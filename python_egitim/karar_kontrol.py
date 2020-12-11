# %% if-elif-else switchcase

sayi = float(input("sayi gir:"))

# if sayi>0:
#     print("pozitif")
# if sayi<0:
#     print("negatif")
# if sayi==0:
#     print("sıfır")

if sayi > 0:
    print("pozitif")
elif sayi < 0:
    print("negatif")
elif sayi == 0:
    print("sıfır")


# %% and or not
dz = 25.0
notort = 79.0
zayifSayisi = 2

# devamsızlık 20 günden fazla ise kesin kalır
# 3ten fazla zayıfı var ama not ortalaması 75ten büyükse kalır
# diğer her durumda geçer

if dz <= 20 and (notort > 75 or zayifSayisi < 3):
    print("geçer")
else:
    print("kaldı")

# %% for döngüsü

# for döngüsü koleksiyonlarda çalışır.
# koleksiyonlar içinde gezer.

s = "hasan"
saya = 0
for harf in s:
    print(harf)
    if harf == "a":
        saya = saya+1
# print("\na sayısı=",saya)


# %%
listem = ["hasan", "hüseyin", 1, 2]

for e in listem:
    print(e)

red = 255, 0, 0  # (255,0,0)

for sayi in red:
    print(sayi)

# %% range koleksiyonu

# 3 kullanımı var

r1 = range(5)

print(r1)

#sıralı koleksiyon tuple, list ve string gibi
# r1[3]=5 tuple ve string gibide değiştirilemez
print(r1[3])

# %% range(ilk,son)
r2=range(20,30)
print(r2[4])

# range(ilk,son,adım)
r3=range(2,50,7)

r4=range(20,5,-2)


# %%

# r5=range("a","z")
#range tam sayı olacak

r5=range(1,2,0.2)
for h in r5:
    print(h)

# %% girilen 2 sayı arasındaki toplam

ilk=int(input("ilk:"))
ikinci=int(input("ikinci:"))
t=0
if ilk>ikinci:
    ilk,ikinci=ikinci,ilk
for s in range(ilk,ikinci+1):
    t=t+s 

print(t)

# %% koleksiyonlar
    #iterable olanlar
    # """
    #     Sözlük(Dictionary)
    #     demet (tuple)
    #     liste(list)
    #     range
    #     karkater dizisi(String)
    #     küme
    # """


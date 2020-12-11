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


#%%
i=0
while i<10:
    print(i)
    i+=1

#i++ ++i --i i-- bunlart atası C dillerdir C syntax
# %%
# i=0
# while (i=i+1)<10:
#     print(i)
    
bolunen=10
bolen=3
bolum=0
kalan=0

while bolunen>=bolen:
    bolunen=bolunen-bolen
    bolum+=1#bolum=bolum+1
kalan=bolunen
print(bolum,kalan)


# %%iç içe while

i=1
j=1 

while i<=3:
    while j<=3:
        print(i*j)
        j=j+1
    i=i+1
    j=1


# %% en büyük toplama sahip alt dizi
fark=[13,-3,-25,20,-30,-16,-23,18,20,
-7,12,-5,-22,15,-4,7]
i=0
j=0
ekbas=0
ekson=0
enkarli=-100000000000#eksi sonsuz
toplam=0
while i<len(fark):
    j=i
    while j<len(fark):
        #print(fark[j],end="",sep="-")
        
        toplam=toplam+fark[j]
        if toplam>enkarli:
            enkarli=toplam
            ekbas=i 
            ekson=j
        j=j+1
    toplam=0
    i=i+1
    #print(toplam)

print(enkarli,ekbas,ekson)

# %%

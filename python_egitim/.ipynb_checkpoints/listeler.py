# %% listeler 
import random
l1=[]#list()
for _ in range(1000):
    l1.append(random.randint(50,100))
# bundan sonraki komutta listedeki 
# çift ve tek elemanların ortalamsının farkını bulun
tt=0;ct=0;tsa=0
i=0
while i<len(l1):
    if l1[i]%2==0:
        ct+=l1[i]
    else:
        tt+=l1[i]
        tsa+=1
    i+=1
fark = ct/(len(l1)-tsa) - tt/tsa
print(fark,ct,tt,tsa)



# %%
l1=[2,3,5,80,30,22,75,63]
tt=0;ct=0;tsa=0
for i in l1:
    if i%2==0:
        ct+=i
    else:
        tt+=i
        tsa+=1

fark = ct/(len(l1)-tsa) - tt/tsa
print(fark,ct,tt,tsa)


# %% Çok boyutlu listeler
reyonlar=[[3,7,8,7],[9,11,13,6],[14,4,2,5],[2,20]]
# print(resim)
# print(resim[1])
# print(resim[3])

for e in resim:
    print(e)
print(10*"-")
for de in resim:
    for e in de:
        print(e,end=" ")
    print()

# %%
reyonlar=[[3,7,8,7],[9,11,13,6],[14,4,2,5],[2,20]]

r0t=0
for r0e in reyonlar[0]:
    pass
# %% dir fonksiyonu

print(dir(list))
# print(dir(int))
# print(dir(tuple))

# %% append
list2=[1,2,3]
list2.append(5)
print(list2)
# %% tüm elemanları temizler
list2.clear()
print(list2)

# %%
list2=[1,2,3]
del list2[1]
print(list2)
print(list2[1])

# %% insert komutu araya elaman ekleme
list2=[1,2,3]
list2.insert(1,8)
print(list2)
list2.insert(-1,10)
print(list2)
list2.insert(0,101)
print(list2)

# %% index eleman kaçıncı sırada 
# olduğunu döndürür eleman yoksa hata üretir
list2=[1,3,4,42,2,3,42]
if 33 in list2:
    print(list2.index(33))
else:
    print(33,"bu listede yok")

if 42 in list2:
    print(list2.index(42))
else:
    print(33,"bu listede yok")

# %% count ise bir listede 
# aranan elemandan kaçtane olduğunu döndürür

print("42 den",list2.count(4332),"adet var")


# %% pop komutu 
# parametre veya arguman almaz ise
# en son elemanı siler ve o değeri döndürür

list2=[1,3,4,42,2,3,42]

print(list2)
print(list2.pop())
print(list2)

# %%

list2=[1,3,4,42,2,3,42]

print(list2)
print(list2.pop(0))
print(list2)
# %% benim pop
list2=[1,3,4,42,2,3,42]
def benimpop(l):
    ese=l[-1]
    del l[-1]
    return ese

print(benimpop(list2))
print(list2)
# %% 
def ikikatiyap(a:int):
    a=2*a 
    return a 

a=5
print(ikikatiyap(a))
print(a)

# %%
# java c c++ c# statik yani 
# kalıcı tiplere sahiptir
# python dart js dinamik tipleri vardır
l1=[1,3,4,42,2,3,42]
l2=l1
print("l1",l1)
print("l2",l2)
l1[0]=399
print("l1",l1)
print("l2",l2)

# %% copy fonskiyonu sadece değerleri aktarır
l1=[1,3,4,42,2,3,42]
l2=l1.copy()#l1=l2[:]

print("l1",l1)
print("l2",l2)
l1[0]=399
print("l1",l1)
print("l2",l2)
# %% sort ve reverse 
# bu işlmeler liste üzerinde ()

l3=[35,36,7,2,58,369]
l3.sort()
print(l3)
l3.reverse()
print(l3)
# %% gereksşz verileri sil
l3=[35,36,7,2,58,369]
l3s=l3.copy()
del l3
l3s.sort()
print(l3s)
l3s.reverse()
print(l3s)

# %% list comprhesions

sifirlar=[i for i in range(1,9) ]
print(sifirlar)

# %%
sifirlar=[i*0 for i in range(1,9) ]
print(sifirlar)
# %% kareler 1 den 10 a kadar sayıların
# karelerinden oluşsan liste

kareler = [i*i for i in range(1,11)]
print(kareler)
# %% iki boyutlu

ikib = [[i*j for j in range(1,4)] for i in range(1,3) ]
print(ikib)

# %% 1-9 arasında sayılardan oluşan 3*3 lük dliste

listem = [[ 3*i+1+j for j in range(0,3)]for i in range(0,3)]
print(listem)
# %% comprehesion önrek 100 elemanlın listede
#çift ve tek sayıları ayrı listelere almak
import random

listem = [ random.randint(1,1000) for i in range(100)]
ciftSayilar = [i for i in listem if i%2==0]
tekSayilar = [i for i in listem if i%2==1]
kucuk500=[i for i in listem if i<=500]
buyuk500=[i for i in listem if i>500]

print(listem)
print("çift sayılar\n",ciftSayilar)
print("tek sayılar\n",tekSayilar)
print("500 den küçükler\n",kucuk500)
print("500den büyüklersayılar\n",buyuk500)
# %% numpy + pandas

# %% break: bu komuta sıra
#  geldiği zaman kendine en yakın döngüyü bitirir

#kullanıcıdan giriş alsın her adımda döngü
#  ve q karakteri girilince döngüyü kırsın
while True:
    g=input("giriş:")
    if g=="q":
        break
    print(g)

# %% kullanıcıdan girilen sayıları toplayan 
# ve q karakteri girilince 
# en son toplam değerini veren python kodunu yazalım

toplam=0
while True:
    g=input("giriş:")
    if g=="q":
        break
    toplam=toplam+int(g)

print(toplam)

# %% continue: bu komuta sıra geldiği zaman kendine en 
# yakın döngü satırına geri döner.
xler=[10,20,3,40]
toplam=0
for x in xler:
    if x==3:
        continue
    toplam+=(1/(3-x))#toplam+=toplam+(1/(3-x))
print(toplam)
# %% Collatz hipotezi
c0=int(input("sayi:"))
step=0

while c0!=1:
    if c0%2==0:
        c0=c0//2
    else:
        c0=3*c0+1
    print(c0)
    step+=1#step=step+1
    

print("adım=",step)
# %% while else
while False:
    print("hiç")
else:
    print("her zaman")

# %% her şartta döngünü çalışan kısmı
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

# %%

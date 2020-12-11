# %% fonksiyonlar

# bir iş yapanlar
print("merhaba")  # built-in

# sonuç döndürenler
a = input("sayı gir:")
print(input("giriş:"))
# %% ilk fonsiyon

# fonksiyon 2 kısımdan oluşur.
# tanım(definition)
# çağırma-gerçekleme(call-invoke)


def ilkFonksiyon():
    print("merhaba dünya")


ilkFonksiyon()

# %% argüman veya parametre


def selam_ver(isim):
    print("merhaba", isim)


selam_ver("hasan")
ad = "pınar"
selam_ver(ad)

# %% birden fazla argüman kullanımı


def dortgen_alani(kk, uk):
    print("alan=", kk*uk)


dortgen_alani(20, 30)
# %% örnek
# ad ve soyad argumanları
# alıp ekrana merhaba ad soyad
# merhaba hasan can


def selam_ver2(ad, soyad, yas):
    print("merhaba", ad, soyad, "yaş=", yas)


selam_ver2("hasan", "can", 13)

# bu argüman kullanımına konumsal yol
# (positional way)
# %% anahtar kelime kullanımı (keywords way)


def selam_ver3(ad, soyad, yas):
    print("merhaba", ad, soyad, "yaş=", yas)


selam_ver3(yas=13, ad="hasan", soyad="can")

# %% karışık(mixing) parametre kullanımı


def hesapla(a, b, c, d):
    sonuc = a+b*c/d
    print("sonuç=", sonuc, "|", a, b, c, d)


hesapla(1, 2, 10, 2)  # konuma bağlı
hesapla(a=10, d=8, b=20, c=3)  # anahtar kelime yolu
hesapla(1, 5, d=3, c=10)  # karışık kullanım
# karışık kullanımda
# ilk önce konuma bağlı argümanlar yazılır en son
# anahtar kelimeye bağlı argümanlar yazılır.
# hesapla(c=8,1,2,d=5)#hata
# hesapla(1,2,d=5,b=8) # hata
print("merhaba", "nasılsın?", sep="½", end="@")
print()
print("merhaba", "nasılsın?", end="½", sep="@")

# %% geriye değer döndürme return


def daire_alani(r):
    alan = 3*r*r
    return alan  # return 3*r*r
   


print("alan=", daire_alani(5))
# print(daire_alani())

# %% bir listeyi parametre olarak alıp liste
# elemanlarının toplamını bulsun ve
# o sonucu geriye döndürsün


def liste_toplami(lst:list):
    t = 0
    for eleman in lst:
        t += eleman  # t=t+eleman
    return t
    print("selam")


h = [1, 2, 30, 52]
sonuc = liste_toplami(h)
print(sonuc)
# %% artık yıl mı?

# 00 ile biten yıllarda 400'e kalansız bölünenler
# bunun dışındaki yıllarda ise 4'e kalansız bölünenler
# artık yıldır


def artikYilMi(yil: int):  # isLeapYear
    if yil % 100 == 0 and yil % 400 == 0:
        return True
    elif yil % 4 == 0 and not(yil % 100 == 0):
        return True
    else:
        return False


print(artikYilMi(2000))  # True
print(artikYilMi(1700))  # False
print(artikYilMi(2104))  # True
print(artikYilMi(2001))  # False
# %% asallık testi
import random

def isPrime(sayi:int):    
    for bolen in range(2,sayi):
        if sayi%bolen==0:
            return False
    return True

print(isPrime(22))
print(isPrime(97))
# %% varsayılan değer default

def hacim_hesapla(a,b=3,c=8):#(a,b=2,c) hata
    return a*b*c

print(hacim_hesapla(2,8,6))
print(hacim_hesapla(2))
print(hacim_hesapla(5,2))

# fonksiyon tanımındasoldan sağa varsayılan değer ,
# verilen argümandan sonra her argümana
# varsayılan değer verilmelidir.

# %% geçerlilik alanı ve global anahtar kelimesi

def bisey():
    x=10
    print(x)

bisey()
print(x)

# %% geçerlilik alanı

x=10
print(id(x))
def bisey2():  
    x=12 
    print(x)
    
    print(id(x))
  
    
print(x)
bisey2()



# %% global


def bisey3():
    global deger
    deger=10
    print(deger)
    deger=25

bisey3()
print(deger)
# %% üçgen olma kuralı 
#ucenMi --> herhangi iki kenarın uzunlukları toplamı diğer iki kenardan büyük olmalı

def ucgenMi(a,b,c):
    return a+b>c and a+c>b and b+c>a

a=float(input("1.kenar"))
b=float(input("2.kenar"))
c=float(input("3.kenar"))
print(ucgenMi(a,b,c))


# %% heron formülü


def ucgen_alani(a,b,c):
    if ucgenMi(a,b,c):
        s=(a+b+c)/2
        alan=(s*(s-a)*(s-b)*(s-c))**.5
        return alan

print(ucgen_alani(1,3,5))#None
print(ucgen_alani(6,8,10))
print(ucgen_alani(3,4,5))#6

# %% faktoryel

#%% metinde alt parçalar arayan fonksiyon

# %%
# sınıf tanımlama
class IlkSinif:
    a = 0


# sınıftannesne turetme
o1 = IlkSinif()#gömülü yapıcı method __init__()
o2 = IlkSinif()
o1.a="merhaba"
print(o1.a)


print(o1.a)
# %%


class Insan:
    def __init__(self, k, b, sr):#yapıcı method, nesnesyi başlatır, fonksiyonlarla aynı yapıadadır.
        self.kilo = k
        self.boy = b
        self.sacRengi = sr

    def yemek_ye(self, miktar):
        self.kilo += miktar

    def spor_yap(self, miktar):
        self.kilo -= miktar

    def bki(self):
        return self.kilo/self.boy**2


i1 = Insan(75, 1.74, "siyah")#bu işlme __init__ methodunu çağırıp sınıfın bir örneği nesne için türetir
i2 = Insan(90, 1.85, "sarı")

print(i1.boy)
print(i1.kilo)
i1.yemek_ye(2)
print(i1.kilo)

i1.spor_yap(3)
print(i1.kilo)
print(i1.bki())

# %%
a=5.0
print(id(a))
a=5
print(id(a))
# %% oop de sahip olma durumuna göre değişkenler
# nesenelere ait değikenler.
#bilgi gizleme kapsülleme
# iki özellik erişim türü ile belirlenir
# public türetilen neseneden bu özelliğe ulaşılabilir
# private sadece sınıf içinden ulaşılabilir.

class Kedi:
    def __init__(self,ad="",renk="sarı",kilo=5):#yapıcı method (instructor)
        self.isim=ad#public
        self.renk=renk#private
        self.__kilo=10#iki alt çizgi bu değeri gizler bu  kapsulleme diye adlandırılır(encapsulation)
        # print(self.isim,"isimli kedi oluştu.","rengi=",self.renk)
        #nesne değişkenlleri
    def __del__(self):#yok edici method çalıştı
        print(self.isim," kedisi ram den silindi.")

    def setKilo(self,kilo):#set properties
        if kilo>0:
            self.__kilo=kilo
            print("kilo değeri verildi")
        else:
            self.__kilo=-kilo
    def getKilo(self):#get properties
        return self.__kilo

k4=Kedi(ad="tekir")
print(k4.getKilo())
print(k4.isim)
# k1=Kedi("mestan","kahve",8)
# k2=Kedi("tekir")
# k3=Kedi("karagöz","siyah")
# k4=Kedi(ad="tırmık")
# k1.renk="mavi"
# k1.setKilo(-3)
# print(k1.getKilo())
# print(k1.isim)
# print(k1.renk)
# del k2



# %% yığın sınıfı yazacağız. 
class Yigin:
    def __init__(self):
        self.__listem=[]
    def push(self,deger):
        self.__listem.append(deger)
    def pop(self):
        se=self.__listem.pop(-1)
        
        return se
    def goruntule(self):
        for i in self.__listem:
            print(i)    

y1=Yigin()
y1.push(10)
y1.push(20)
y1.push(30)
y1.push(40)
y1.goruntule()
print(y1.pop())
print(30*"-")
y1.goruntule()


# %% kuyruk sınıfı size ait olacak.

class Kuyruk:
    def __init__(self,*degerler):
        self.__listem=[]
        for i in degerler:
            self.__listem.append(i)
    def push(self,deger):
        self.__listem.append(deger)
    def pop(self):
        se=self.__listem.pop(0)
        
        return se
    def goruntule(self):
        for i in self.__listem:
            print(i)    
k1=Kuyruk(305,356,365)
k1.push(10)
k1.push(20)
k1.push(30)
k1.push(40)
k1.goruntule()
print(k1.pop())
print(30*"-")
k1.goruntule()
# %% fonksiyonlara iteratif veri girişi *
def notHesapla(adi:str,soyadi:str,*notlar):
    print(type(notlar))
    ort=0
    for nt in notlar:
        ort+=nt
    return ort/len(notlar)
print(notHesapla("mehmet","gün",30,40,80,60,50))

# %% fonksiyoınlara dict sözlük yapısı giriş **

def f1(a,b,*c,**d):
    print(type(c))
    print(type(d))

f1(1,2,3333,5,55,58,78,{1:"8",2:"10"})

# %% koleksiyoınlar arası dönüşüm
a={1:"8",2:"10"}

print(list(a.keys()))
print(list(a))
print(list(a.values()))
l1=[0,1]
l1.append(a)
print(l1[2])
print(type(l1[2]))
print((l1[2].values()))

# %% sınıfa ait özellik ve davranışlar
#$ bazı özellik ve davarnışlar sınıfa ait tanımlanmak istenebir

class Hayvan:
    adet=0
    def __init__(self,ad="yok",renk="sarı",kilo=5):#yapıcı method (instructor)        
        self.isim=ad#public
        self.renk=renk#
        self.arttir()
        self.__kilo=10#iki alt çizgi bu değeri gizler bu  kapsulleme diye adlandırılır(encapsulation)
        # print(self.isim,"isimli kedi oluştu.","rengi=",self.renk)
        #nesne değişkenlleri
    # def __del__(self):#yok edici method çalıştı
    #     print(self.isim," kedisi ram den silindi.")
    @classmethod
    def arttir(cls):
        cls.adet+=1
    def setKilo(self,kilo):#set properties
        if kilo>0:
            self.__kilo=kilo
            print("kilo değeri verildi")
        elif kilo==0:
            pass
        else:
            self.__kilo=-kilo
    def getKilo(self):#get properties
        return self.__kilo

h1=Hayvan(ad="tekir")

h2=Hayvan(ad="tekir")

h3=Hayvan(ad="tekir")


print(h1.isim)

h1.isim="miyav"
print(h1.isim)
print(h1.getKilo())#private
h1.setKilo(0)
print(h1.getKilo())#private
# print(dir(Hayvan))
print(Hayvan.adet)


# %% hesap sınıfı

class Hesap:
    degerler=[0]#sınıfa ait özellik
    @classmethod#sınıfın methodu olarak işaretle 
    def topla(cls):#burada sınıfa ait çzelliklere ulaşmak için clsyi kullanıyoru
        toplam=0
        for a in cls.degerler:
            toplam+=a
        return toplam

Hesap.degerler.append(3)

print(Hesap.topla())
print(h1.getKilo())
# %% sınıf tanı yapalım
# Araba sınıfı olsun
# Araba sınıfından oluşan 
# nesnelere ait
# renk, marka, model özellikleri olsun 
# renk değiştir methodu olsun 1 parametre alsın
# sınıfa ait ise 
# adet bilgisi olsun kaç tane nesne üretilmiş
# bu sınıfa aitt adet_arttir davranışı olsun

class Araba:
    adet=0
    def __init__(self,r:str="sarı",m:str="marka",md:int=1990):
        self.renk=r
        self.marka=m
        self.model=md
        self.arttir()
    
    def renk_degistir(self,re:str):
        self.renk=re
    @classmethod
    def arttir(cls):
        cls.adet+=1
    def __del__(self):
        print("bir araba silindi")

    

arabalar=[]

for _ in range(30):
    araba=Araba()
    arabalar.append(araba)

print(Araba.adet)
del arabalar[0]
# sınıfa ait methodlar @classmethod ile tanımlanır.

#%% örnek miras alma
class dizi(list):
    def toplam(self):
        toplam=0
        for i in self.copy():
            toplam+=i
        return toplam

a=dizi()

a.append(20)
a.append(30)
a.append(40)

print(a.toplam())
# %% miras
# punlic davranş ve özellikler miras verilir
# private davranış ve özellikler miras verilmez

# method eğer sınıfta tanımlı değilse ata sınıfa
# baklır. Eğer sınıfta tanımlı ise o metod çalıştırılır. buna method ezme(override) denir.
class Hayvan:
    def __init__(self,ad):#method ezme(override)
        self.ad=ad
        # self.yas=10
        print(self.ad,"Hayanı oluşturuldu.")
    def ses_cikar(self):
        print(self.ad,"hayvanı ses çıkardı.")
    def getYas(self):
        return self.yas

class Kedi(Hayvan):
    def __init__(self,isim):#methoıd ezme
        # super().__init__(self,isim)
        self.ad=isim
        print(self.ad,"kedi yapıcı")
    def ses_cikar(self):#method ezme
        print("miyav..")

class Kopek(Hayvan):
    def ses_cikar(self):#bu method ezmne değildir.
        print("hav hav...")

class Kus(Hayvan):
    def ses_cikar(self):
        print("cik cik")



h1 = Hayvan("hayvan")
kd1 = Kedi("minnoş")
print(kd1.getYas())
kp1 = Kopek("karabaş")
limon=Kus("limon")
h1.ses_cikar()
kp1.ses_cikar()
kd1.ses_cikar()
limon.ses_cikar()
# %% çok biçimlilik

def haynavlar_ses_cikarsin(nesne):
    if isinstance(nesne,Hayvan):
        nesne.ses_cikar()
    else:
        print("bana hayvan vermelisin")

haynavlar_ses_cikarsin(limon)
haynavlar_ses_cikarsin(kd1)
haynavlar_ses_cikarsin(kp1)
haynavlar_ses_cikarsin(h1)
liste=[]
haynavlar_ses_cikarsin(liste)

# %%

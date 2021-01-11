#%%

l = [0 for i in range(10_000_000)]
print(len(l))
# %%
import numpy as np
l1 = np.zeros(100_000_000)
print(l1.size)
print(l1.dtype)
# %% numpy temel yapısı
import numpy as np
nd1 = np.array([1,2,3])
print(nd1.size)
print(nd1.shape)
print(nd1.dtype)
print(nd1.ndim)
print(type(nd1))

# %% 0-D yani buna skaler bir yapı 
#standadrt değişken
nd0 = np.array(38)
print(nd0.size)
print(nd0.shape)
print(nd0.dtype)
print(nd0.ndim)
print(type(nd0))
# %% 1-D
nd1 = np.array([38,25,38])
print(nd1.size)
print(nd1.shape)
print(nd1.dtype)
print(nd1.ndim)
print(type(nd1))
# %% 2-D
l= [[1,2],[3,4]]
nd2 = np.array(l,dtype=np.uint8)
print(nd2.size)
print(nd2.shape)
print(nd2.dtype)
print(nd2.ndim)
print(type(nd2))
# %% 3-D
# arange, randint, linspace, zeros, ones,full
import numpy as np
l = [[[1,2,3],[4,5,6],[7,8,9]]]

nd3 = np.array(l,dtype=np.float16)
print(nd3.size)
print(nd3.shape)
print(nd3.dtype)
print(nd3.ndim)
print(nd3)



# %% düzgün şekilli olmalı
import numpy as np
l= [[1,2,3],[3,4,5,6]]
nd2 = np.array(l)
print(nd2.size)
print(nd2.shape)
print(nd2.dtype)
print(nd2.ndim)
print(type(nd2))
print(nd2)
# %% ndarray elemanlarına ulaşma
#arange belli aralıktaki sayılar ile np.array oluşturur
# aynı range gibi

ndt1 = np.arange(12)
print(ndt1)
print(ndt1[3])
ndt1[3]=333
print(ndt1)

# %% 0 lardan oluşan (3,3,3) bouyutlu bir dizi

ndz0 = np.zeros((3,3),dtype=np.float32)
print(ndz0)
print("*"*20)
ndz0[2,1]=33
print(ndz0)

# %% elemanlara erişim
nd7 = np.array([1, 2, 3, 4])
nd8 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
nd9 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(nd7[1])#2
print(nd8[1, 2])#8
print(nd9[0, 1, 2])#6
# %% ones zeros gibi sadece belirtilen şekilde 
# birlerden oluşan bir dizi tanımlar.
# full
ndf0 = np.full((3,4),"bilsem")
print(ndf0)

# %% rastgele sayılardan oluşturalım
ndr0 = np.random.randint(0,255,(4,4),dtype=np.uint8)
print(ndr0)
ndr0[1]=255
print(30*"*")
print(ndr0)

# %% slice biçme iişlemleri
ndr1 = np.arange(12)
print(ndr1.shape)
ndr1.shape=(3,4)# bu komut dizi şeklkini değiştirdi
print(ndr1.shape)
print(ndr1)
print("\n",ndr1[0,:])#0. satırı verir
print("\n",ndr1[0:1,:])#0. satırı 2 boyutlu olarak verir
print("\n",ndr1[0:2,:])#0. satırı 2 boyutlu olarak verir
print("\n",ndr1[2,2:])#2. satırdaki 2.sütun sonrası
print("\n",ndr1[1:,1:3])


# %%
# %% kopya ve görüntü (copy and view)
# Bir dizinin kopyası ile görünümü arasındaki temel fark, kopyanın yeni bir dizi olması ve görünümün yalnızca orijinal dizinin bir görünümü olmasıdır.

# Kopya(copy) verinin sahibidir ve kopyada yapılan herhangi bir değişiklik orijinal diziyi etkilemeyecektir ve orijinal dizide yapılan herhangi bir değişiklik kopyayı etkilemeyecektir.

import numpy as np
n15 = np.array([1, 2, 3, 4, 5])
x = n15.copy()# hiçbirşeyden etkilenmemek için
y = n15.view()# ana kopyadaki değişiklik diğerlerine de etki etsin istenirse view
n15[0] = 42

print(n15)
print(x, "--", x.base)
print(y, "--", y.base)

x[4] = 55
y[3] = 44
print(20*"-")
print("n15:", n15)
print("x:", x, "--", x.base)
print("y:", y, "--", y.base)

# %% skalare işlemler
import numpy as np

a = np.array([[1, 2],[3, 4]])
b = np.array([[40, 30],[20, 10]])

print("skaler işlemler:")
print("a+1:",a+1,end="\n\n")
print("a*2:",a*2,end="\n\n")
print("b/3:",b/3,end="\n\n")
print("b-2:",b-2,end="\n\n")
print("np.sgrt(a):",np.sqrt(a),end="\n\n")
print("a*a:",a*a,end="\n\n")
print("a+b:",a+b,end="\n\n")# ayı şekle sahip olanlar da 4 işlem yapılabilir.
# %%

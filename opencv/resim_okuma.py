import cv2 #opencv
import os # operating system
import numpy as np

cd = os.getcwd() #current directory bilgisi
# print(cd)
image_path = os.path.join(cd,"opencv","images","chp1","marsrover.png")
# resim image değişkenine aktartılıyor
image = cv2.imread(image_path)
o_image=image.copy()
# image = image[::2,::2,:]
print(type(image),image.dtype)
#resmin dizi oalrak boyutunun bulunması
shape = image.shape
print(shape)
h = shape[0]
w = shape[1]
print(f"resmin boyutu: {w}*{h}")

# bir pikselin renk bilgisi
ilk_renk = image[0,0]
print(ilk_renk,type(ilk_renk))
# bir grup pikselin rengini değiştirelim
image[0:100,0:200]=ilk_renk#[0,255,0]

#bir çizgi çizelim c2.line(resim,start,end,color,thikness)
baslangic = (100,70)#orta nokta
bitis =(350,380)
cizgi_rengi = (0,255,0)
kalinlik = 4
cv2.line(image,baslangic,bitis,cizgi_rengi,kalinlik)
#aynı değerler il ebir dikdörtgen çizelim
cv2.rectangle(image,baslangic,bitis,cizgi_rengi,kalinlik)

cv2.imshow("islenmis resim ",image)
cv2.imshow("orijinal",o_image)
cv2.waitKey(0)

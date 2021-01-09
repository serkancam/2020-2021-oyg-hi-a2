import cv2
import os

cd = os.getcwd()
# print(cd)
image_path = os.path.join(cd,"opencv","images","road.jpg")
# print(image_path)
image = cv2.imread(image_path)
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
print(ilk_renk)
# bir grup pikselin rengini değiştirelim
image[0:100,0:200]=ilk_renk

#bir çizgi çizelim c2.line(resim,start,end,color,thikness)
baslangic = (w//2,h//2)#orta nokta
bitis =(w,h)
cizgi_rengi = (0,0,255)
kalinlik = 5
cv2.line(image,baslangic,bitis,cizgi_rengi,kalinlik)
#aynı değerler il ebir dikdörtgen çizelim
cv2.rectangle(image,baslangic,bitis,cizgi_rengi,kalinlik)

cv2.imshow("yol",image[::2,::2])
cv2.waitKey(0)

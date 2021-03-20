import cv2
import os
import numpy as np

cd = os.getcwd()

image_path = os.path.join(cd, "opencv", "images", "chp2", "zebra.png")
zebra_o = cv2.imread(image_path)

# resize işlemi
h, w, c = zebra_o.shape#(1056,920,3)

# en boy oranı aspect ratio
aspect = w/h
# yeni boyutları hesapladık
h_new = int(h*0.5)
w_new = int(h_new*aspect)
dimension = (h_new,w_new)
# bu boyut bilgisi ile boyutlandırma yaptık
zebra_r1 = cv2.resize(src=zebra_o,dsize=dimension,interpolation=cv2.INTER_CUBIC)
# genişlik ve yüksekli değerlerini el girerek boyutlandırma
zebra_r2 = cv2.resize(src=zebra_o,dsize=None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)


### sonuçları görtüntüler ###
cv2.imshow("Original", zebra_o)
cv2.imshow("R1", zebra_r1)
cv2.imshow("R2", zebra_r2)
cv2.waitKey(0)

# INTER_LINEAR: Bu aslında en yakın dört komşunun (2 × 2 = 4) belirlendiği ve bir sonraki pikselin değerini belirlemek için ağırlıklı ortalamasının hesaplandığı bir çift doğrusal enterpolasyondur. 

# INTER_NEAREST: Bu, o noktanın etrafındaki noktalarda (komşu) noktalarda o fonksiyonun değeri verildiğinde, bir boşluktaki bir olmayan nokta için bir fonksiyonun değerini tahmin etmek için en yakın komşu enterpolasyon yöntemini kullanır. Başka bir deyişle, bir pikselin değerini hesaplamak için, en yakın komşusunun enterpolasyon fonksiyonuna yaklaştığı kabul edilir. 

# INTER_CUBIC: Bu, piksel değerini hesaplamak için bikübik enterpolasyon algoritması kullanır. Çift doğrusal enterpolasyona benzer şekilde, bir sonraki pikselin değerini belirlemek için 4 × 4 = 16 en yakın komşuyu kullanır. Hız bir sorun olmadığında, bikübik enterpolasyon, çift doğrusal ile karşılaştırıldığında daha iyi yeniden boyutlandırılmış bir görüntü sağlar. 

# INTER_LANCZOS4: Bu, 8 × 8 en yakın komşu enterpolasyonunu kullanır. 

# INTER_AREA: Piksel değerinin hesaplanması, piksel alanı ilişkisi kullanılarak gerçekleştirilir (OpenCV resmi belgelerinde açıklandığı gibi). Bu algoritmayı hareli olmayan yeniden boyutlandırılmış bir görüntü oluşturmak için kullanıyoruz. Görüntü boyutu büyütüldüğünde, INTER_AREA INTER_NEAREST yöntemine benzer.
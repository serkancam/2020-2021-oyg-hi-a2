import cv2
import numpy as np
import os

image_path = os.path.join(os.getcwd(),"opencv","images","chp2","scanned_doc.png")
# image_path = os.path.join(os.getcwd(),"opencv","images","chp2","sudoku.jpg")
image=cv2.imread(image_path)
print("image:",image.shape)
cv2.imshow("orijinal image",image)
#gri
gri = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
print("gri:",gri.shape)
cv2.imshow("gri",gri)
# binarization(ikileştirme) veriyi sadece iki farklı değerle ifade etme
# threshold(eşikleme) 
(T,binarized_image) = cv2.threshold(gri,80,255,cv2.THRESH_BINARY)
print("binary_image",binarized_image.shape)
cv2.imshow("binary image",binarized_image)
# thresh_binary_inverse
(Ti,binarized_image_inv) = cv2.threshold(gri,80,255,cv2.THRESH_BINARY_INV)

cv2.imshow("binarized_image_inv",binarized_image_inv)
cv2.waitKey(0)
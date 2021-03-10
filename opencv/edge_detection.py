import cv2
import numpy as np
import os

resim_yolu = os.path.join(os.getcwd(),"opencv","images","chp2","sudoku.jpg")
resim = cv2.imread(resim_yolu)
cv2.imshow("orijinal",resim)
gri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
gri = cv2.bilateralFilter(gri,5,50,50)

# bulanık(blur) halini
sobelx = cv2.Sobel(gri,cv2.CV_64F,1,0,ksize=3)
sobelx = np.uint8(np.absolute(sobelx))
# print(sobelx)
cv2.imshow("sobel x",sobelx)
# -16.0
# 16.0
# 16
sobely = cv2.Sobel(gri,cv2.CV_64F,0,1,ksize=3)
sobely = np.uint8(np.absolute(sobely))
cv2.imshow("sobel y",sobely)
# laplace 
laplace = cv2.Laplacian(gri,cv2.CV_64F)
laplace = np.uint8(np.absolute(laplace))
print(laplace)
cv2.imshow("laplace",laplace)
# canny 
canny = cv2.Canny(resim,50,170)
print(canny)
cv2.imshow("canny",canny)
cv2.waitKey(0)
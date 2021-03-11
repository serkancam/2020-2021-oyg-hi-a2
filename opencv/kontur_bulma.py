import os
import cv2
import numpy as np
yol = os.path.join(os.getcwd(),"opencv","images","chp2","elmalar3.jpg")
resim = cv2.imread(yol)
# resim2 = cv2.bilateralFilter(resim,11,50,50)
gri=cv2.cvtColor(resim
,cv2.COLOR_BGR2GRAY)
_,sbResim = cv2.threshold(gri,110,255,cv2.THRESH_BINARY)
konturlar,_=cv2.findContours(sbResim,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
## elle onturları çizdirmek
# center = (konturlar[0][1][0][0],konturlar[0][1][0][1])
# cv2.circle(resim,center,5,(0,0,255),-1)
# center = (konturlar[0][0][0][0],konturlar[0][0][0][1])
# cv2.circle(resim,center,5,(0,0,255),-1)
# center = (konturlar[0][2][0][0],konturlar[0][2][0][1])
# cv2.circle(resim,center,5,(0,0,255),-1)
# center = (konturlar[0][3][0][0],konturlar[0][3][0][1])
# cv2.circle(resim,center,5,(0,0,255),-1)
# cv2.imshow("resim",resim)
print(len(konturlar))
for knt in konturlar:
    deger = cv2.approxPolyDP(knt,0.009*cv2.arcLength(knt,True),True)
    cv2.drawContours(resim,[deger],0,(0,255,0),2)
cv2.imshow("resim",resim)
cv2.waitKey(0)
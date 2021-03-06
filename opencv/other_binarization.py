import cv2
import os
import numpy as np

image=cv2.imread(os.path.join(os.getcwd(),"opencv","images","chp2","scanned_doc.png"))
cv2.imshow("image",image)
# gir
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
binarized = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,33)
cv2.imshow("binarized",binarized)


cv2.waitKey(0)

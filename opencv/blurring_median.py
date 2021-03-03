import cv2
import os
import numpy as np

image_path = os.path.join(os.getcwd(),"opencv","images","chp2","salt-pepper.jpg")

image = cv2.imread(image_path)
cv2.imshow("orinal resim",image)

blurred_image3 = cv2.(image,3)
cv2.imshow("blurred_image3",blurred_image3)

blurred_image5 = cv2.medianBlur(image,5)
cv2.imshow("blurred_image5",blurred_image5)

blurred_image7 = cv2.medianBlur(image,7)
cv2.imshow("blurred_image7",blurred_image7)

cv2.waitKey(0)

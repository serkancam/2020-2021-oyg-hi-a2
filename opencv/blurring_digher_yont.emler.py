import cv2
import os
import numpy as np

# unix sistemlerde path ayracı /
cd = os.getcwd()
image_path = os.path.join(cd,"opencv","images","chp2","n3.jpg") 
#E:\\yillar\\2020-2021\\dersler\\oyg\\2020-2021-oyg-hi-a2\\opencv\\images\\chp2\\park.jpg"

image =cv2.imread(image_path)
cv2.imshow("resim",image)

gaussianFiltering = cv2.GaussianBlur(image,(7,7),0)
cv2.imshow("gaussianFiltering",gaussianFiltering)

bilateralFiltering = cv2.bilateralFilter(image,7,150,150)
cv2.imshow("bilateralFiltering",bilateralFiltering)
cv2.waitKey(0)
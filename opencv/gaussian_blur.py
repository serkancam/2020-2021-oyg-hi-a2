import cv2
import os
import numpy as np

# unix sistemlerde path ayracı /
cd = os.getcwd()
image_path = os.path.join(cd,"opencv","images","chp2","yuz.jpg") 
#E:\\yillar\\2020-2021\\dersler\\oyg\\2020-2021-oyg-hi-a2\\opencv\\images\\chp2\\park.jpg"

image =cv2.imread(image_path)
cv2.imshow("resim",image)

gaussianFiltering = cv2.GaussianBlur(image,(109,109),0)
cv2.imshow("gaussianFiltering",gaussianFiltering)


cv2.waitKey(0)
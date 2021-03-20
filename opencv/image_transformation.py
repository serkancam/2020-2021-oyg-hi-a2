import cv2
import numpy as np
import os

cd = os.getcwd()
image_path = os.path.join(cd,"opencv","images","chp2","zebrasmall.png")
image_original = cv2.imread(image_path)
image_original = cv2.resize(image_original,None,fx=.5,fy=.5,interpolation=cv2.INTER_AREA)


h,w,c =image_original.shape
center1 = (w//2,h//2)
angle1 = -45
scale1 = 1.0
center2 = (0,0)
angle2 = 15
scale2 = 1.0
#  rotation_matrix
rotate_matrix1 = cv2.getRotationMatrix2D(center1,angle1,scale1)
rotate_matrix2 = cv2.getRotationMatrix2D(center2,angle2,scale2)
# rotate image
image_rotate1 = cv2.warpAffine(src=image_original,M=rotate_matrix1,dsize=(w,h))  
image_rotate2 = cv2.warpAffine(src=image_original,M=rotate_matrix2,dsize=(w,h))  
# flip image
image_flip_vertically = cv2.flip(image_original,0)# vertical 0 horizantal 1 herikis için -1
# image show
cv2.imshow("original",image_original)
cv2.imshow("rotate1",image_rotate1)
cv2.imshow("rotate2",image_rotate2)
cv2.imshow("vertical flip",image_flip_vertically)

cv2.waitKey(0)
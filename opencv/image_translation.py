import cv2
import os
import numpy as np

cd = os.getcwd()
image_path=os.path.join(cd,"opencv","images","chp2","soccer-in-green.jpg")
# print("**",cd,"**")
image = cv2.imread(image_path)
h,w,c=image.shape
dimension = (h,w)
# döşüşüm(translation) matrisi
dm = np.float32([[1,0,50],[0,1,20]])
image_t = cv2.warpAffine(src=image,M=dm,dsize=dimension)

cv2.imshow("Orginal",image)
cv2.imshow("Translation",image_t)

cv2.waitKey(0)




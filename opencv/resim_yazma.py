import cv2
import os
import numpy as np
cd = os.getcwd()
canvas_r = np.zeros((200,200,3),dtype= np.uint8)
canvas_c = canvas_r.copy()

start = (0,0)
end =(100,100)
c_center=(100,100)
radius = 50
color_c = (255,0,0)
color_r = (255,255,0)
thickness_r=2
thickness_c=2
cv2.rectangle(canvas_r,start,end,color_r,thickness_r)
cv2.circle(canvas_c,c_center,radius,color_c,thickness_c)

cv2.imshow("rectangle",canvas_r)
cv2.imshow("circle",canvas_c)
# oluşanb imajları kayır edelim
c_path = os.path.join(cd,"opencv","images","chp1","circle.jpg")
r_path = os.path.join(cd,"opencv","images","chp1","rectangle.jpg")

cv2.imwrite(c_path,canvas_c)
cv2.imwrite(r_path,canvas_r)

cv2.waitKey(0)



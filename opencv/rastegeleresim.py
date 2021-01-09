# %%
import cv2
import numpy as np
image = np.random.randint(0, 255, size=(600, 600, 3), dtype=np.uint8)
cv2.imshow("test",image)
cv2.waitKey(0)
# %%

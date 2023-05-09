import numpy as np
import cv2

H, W = 480, 480
blank_image = np.zeros((H,W,4), np.uint8)
cv2.imwrite('image_alpha.png', blank_image)
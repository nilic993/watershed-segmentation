import cv2
import numpy as np

img = cv2.imread('test.png')
img_copy = np.copy(img)

marker_image = np.zeros(road.shape[:2],dtype=np.int32)

segments = np.zeros(road.shape,dtype=np.uint8)

import cv2
import numpy as np

# Inputs

img = cv2.imread('test.png')
img_copy = np.copy(img)

marker_image = np.zeros(road.shape[:2],dtype=np.int32)
segments = np.zeros(road.shape,dtype=np.uint8) # Empty

# Global variables

current_marker = 1
colors = [] # TO DO add colors

# Markers
markers_updated = False

# Callback function

def mouse_callback(event,x,y,flags,param):
	global markers_updated
	
	if event == cv2.EVENT_LBUTTONDOWN:
	
		# Markers passed to watershed algorithm
		cv2.circle(marker_image,(x,y),10,(current_marker),-1)
		
		# Markers visible to user
		cv2.circle(img_copy,(x,y),10,colors[current_marker],-1)
		
		markers_updated = True

# WHILE TRUE

#cv2.namedWindow('Watershed')
#cv2.setMouseCallback('Road Image', mouse_callback)


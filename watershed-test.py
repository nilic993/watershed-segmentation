import cv2
import numpy as np
from matplotlib import cm

# Inputs

# TO DO: Change the way images are loaded

img = cv2.imread('img/test.jpg')
img_copy = np.copy(img)

marker_image = np.zeros(img.shape[:2],dtype=np.int32)
segments = np.zeros(img.shape,dtype=np.uint8) # Empty

n_markers = 10
current_marker = 1

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

# Colors		
	
def create_rgb(i):
	return tuple(np.array(cm.tab10(i)[:3])*255)
	
colors = []

for i in range(10):
	colors.append(create_rgb(i)) 

while True:

	cv2.imshow('Watershed Segments', segments)
	cv2.imshow('Original image', img_copy)
	cv2.setMouseCallback('Original image', mouse_callback)
	
	# Close windows
	
	k = cv2.waitKey(1)
	
	if k == 27:	# Escape key
		break
		
	# Clearing colors:
	
	elif k == ord('c'): # Reset colors with 'c'
		img_copy = img.copy()
		marker_image = np.zeros(img.shape[:2],dtype=np.int32)
		segments = np.zeros(img.shape,dtype=np.uint8)
	
	# Update colors
	
	elif k > 0 and chr(k).isdigit(): # choose color
		current_marker = int(chr(k))
	
	# Update markers
	
	if markers_updated:
		marker_image_copy = marker_image.copy()
		cv2.watershed(img,marker_image_copy)
		
		segments = np.zeros(img.shape,dtype=np.uint8)
		
		for color_ind in range(n_markers):
			# Color the segments
			segments[marker_image_copy==(color_ind)] = colors[color_ind]

cv2.destroyAllWindows()






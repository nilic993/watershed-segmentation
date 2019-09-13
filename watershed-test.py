import cv2
import numpy as np

# Inputs

img = cv2.imread('test.png')
img_copy = np.copy(img)

marker_image = np.zeros(img.shape[:2],dtype=np.int32)
segments = np.zeros(img.shape,dtype=np.uint8) # Empty

n_markers = 10
current_marker = 1
colors = [(31.0, 119.0, 180,0),(255.0, 127.0, 14.0),(44.0, 160.0, 144.0),(214.0, 39.0, 40.0),(148.0, 103.0, 189.0),(140.0, 86.0, 75.0),(227.0, 119.0, 194.0),(127.0, 127.0, 127.0),(188.0, 188.0, 34.0),(23.0, 190.0 ,209.0)]

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

#cv2.namedWindow('Watershed')
cv2.setMouseCallback('Watershed', mouse_callback)

while True:

	cv2.imshow('Watershed Segments', segments)
	cv2.imshow('Original image', img_copy)
	
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






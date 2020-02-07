import cv2
import numpy as np
import os
from matplotlib import cm

def add_overlay(base_img, transp_img, transp_weight):
    added_image = cv2.addWeighted(base_img, 1.0, transp_img, transp_weight, 0)
    return added_image

# Inputs

img_folder = "./img/"
res_s_folder = "./res_s/"
load_im = 'path'

if not os.path.exists(img_folder): # If directories missing + image path
    os.makedirs(img_folder)
if not os.path.exists(res_s_folder):
    os.makedirs(res_s_folder)
while not os.path.exists(img_folder+load_im):
    load_im = input("Enter filename (example: 1.jpg): ")

img = cv2.imread(os.path.join(img_folder, load_im)) # Input image
img_copy = np.copy(img)

marker_image = np.zeros(img.shape[:2],dtype=np.int32)
segments = np.zeros(img.shape,dtype=np.uint8) # Empty

n_markers = 10
current_marker = 1
s = 0

# Markers
markers_updated = False

# Callback

def mouse_callback(event,x,y,flags,param):
    global markers_updated

    if event == cv2.EVENT_LBUTTONDOWN:

        # Markers passed to watershed algorithm
        cv2.circle(marker_image,(x,y),10,(current_marker),-1)

        # Markers visible to user
        cv2.circle(img_copy,(x,y),10,colors[current_marker],-1)

        markers_updated = True


def create_rgb(i): # Colors
    return tuple(np.array(cm.tab10(i)[:3])*255)
colors = []
for i in range(10):
    colors.append(create_rgb(i))

print("***WATERSHED SEGMENTATION***\n\
*Assign color with numeric keys (1-9)\n\
*Click on input image to segment\n\
*Save segments with S, original image + segments with T, clear colors with C\n\
*Press Escape to quit")

while True:

    cv2.imshow('Watershed Segments', segments)
    cv2.imshow('Original image', img_copy)
    cv2.setMouseCallback('Original image', mouse_callback)

    k = cv2.waitKey(1)

    if k == 27:    # Escape key
        break

    elif k == ord('s'): # Save segmented image with 's'
        cv2.imwrite(res_s_folder+'segmentation_'+str(s)+'_'+load_im, segments)
        s = s + 1

    elif k == ord('t'): # Save segmented image with 't'
        transp_img = add_overlay(img, segments, 0.8)
        cv2.imwrite(res_s_folder+'transp_segmentation_'+str(s)+'_'+load_im, transp_img)
        s = s + 1

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

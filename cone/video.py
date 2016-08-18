import cv2
import glob
import time
import numpy as np

images = glob.glob("/home/pi/Desktop/cone/real/*.jpg")
#print images

images.sort()
tmp_list = images[0].split('/')
title = tmp_list[-1] 

image = cv2.imread(images[0])


height , width , layers =  image.shape



video = cv2.VideoWriter('/home/pi/Desktop/cone/video.avi',cv2.cv.CV_FOURCC('M','J','P','G'),1,(640,240))

for name in images:
	tmp_list = name.split('/')
	title = tmp_list[-1] 
	image_real = cv2.imread("/home/pi/Desktop/cone/real/"+title)
	image_filtered = cv2.imread("/home/pi/Desktop/cone/filtered/"+title)
	vis = np.concatenate((image_real, image_filtered), axis=1)
	time.sleep(0.1)

	cv2.imshow("vis",vis)
	key = cv2.waitKey(1) & 0xFF
	video.write(vis)

video.release()


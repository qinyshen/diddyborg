# import the necessary packages
import numpy as np
import cv2
import serial
from picamera.array import PiRGBArray
from picamera import PiCamera
import picamera
import time

KNOWN_DISTANCE = 12.0

KNOWN_WIDTH = 4.5

focalLength = 221



def find_marker(image):
	# convert the image to grayscale, blur it, and detect edges
	image_R = cv2.medianBlur(image, 5)
        image_R = cv2.cvtColor(image_R, cv2.COLOR_RGB2HSV) # Swaps the red and blue channels!
	red = cv2.inRange(image_R, np.array((115, 127, 64)), np.array((125, 255, 255)))
#	cv2.imshow("red", red)
	
	contours,hierarchy = cv2.findContours(red, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	
	c = max(contours, key = cv2.contourArea)

	# compute the bounding box of the of the paper region and return it
	return cv2.minAreaRect(c)



def distance_to_camera(knownWidth, focalLength, perWidth):
	# compute and return the distance from the maker to the camera
	return (knownWidth * focalLength) / perWidth
 

def distance(image):
	marker = find_marker(image)
	inches = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])
	return inches

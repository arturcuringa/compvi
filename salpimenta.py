import numpy as np
import cv2
import sys

if __name__ == '__main__':
	img_path = sys.argv[1]
	img = cv2.imread(img_path, 0)
	result = cv2.medianBlur(img, 5)
	cv2.imshow('aaa', result)
	cv2.waitKey()
	

import numpy as np
import cv2
import sys

if __name__ == '__main__':
	img_path = sys.argv[1]
	truth = sys.argv[2]
	img = cv2.imread(img_path, 0)
	img_truth = cv2.imread(truth, 0)
	result = cv2.GaussianBlur(img, ( 7, 7), 0)
	cv2.imwrite('gaussian7x7.jpg', result)
	print(np.sqrt(np.mean((img_truth.astype(int).flatten() - result.astype(int).flatten()) ** 2)))
	cv2.imshow('aaa', result)
	cv2.waitKey()
	

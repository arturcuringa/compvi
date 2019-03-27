import matplotlib.pyplot as plt
import cv2
import sys

if __name__ == '__main__':
	img_path = sys.argv[1]
	img = cv2.imread(img_path, 0)
	plt.hist(img.flatten(), bins=255)
	plt.show()

import sys
import cv2
import glob
import os
import numpy as np


if __name__ == '__main__':
    img_path = glob.glob(os.path.join(sys.argv[1], '*.jpg'))
    img_list = np.array([cv2.imread(img,0) for img in img_path], dtype=int)
    img = sum(img_list) /len(img_list) 
    img = np.array(img, dtype=np.uint8)
    cv2.imshow('mean', img)
    cv2.waitKey(0)


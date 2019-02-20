import sys
import cv2
import numpy as np


if __name__ == '__main__':

    img1_path = sys.argv[1]
    img2_path = sys.argv[2]
    img1 = cv2.imread(img1_path, 1)
    img2 = cv2.imread(img2_path, 1)
    max_shape = (min(img1.shape[0], img2.shape[0]), min(img1.shape[1], img2.shape[1]))
    img1 = np.array(img1[:max_shape[0], :max_shape[1], :])
    img2 = np.array(img2[:max_shape[0], :max_shape[1], :])
    cv2.imshow('c', img1)
    cv2.waitKey(0)
    cv2.imshow('c', img2)
    cv2.waitKey(0)
    c = img1 // 2 + img2 // 2 
    cv2.imshow('c', c)
    cv2.waitKey(0)

import sys
import cv2
import numpy as np
import numpy as np


def split_channel(img):
    r = np.zeros(img.shape, dtype=np.uint8)
    b = np.zeros(img.shape, dtype=np.uint8)
    g = np.zeros(img.shape, dtype=np.uint8)
    r[:, :, 2] = img[:,:,2]
    g[:, :, 1] = img[:,:,1]
    b[:, :, 0] = img[:,:,0]

    return r, g, b


if __name__ == '__main__':
    img_path = sys.argv[1]
    img = cv2.imread(img_path, 1)
    b, g, r = split_channel(img)
    cv2.imshow('B', b)
    cv2.waitKey(0)
    cv2.imshow('G', g)
    cv2.waitKey(0)
    cv2.imshow('R', r)
    cv2.waitKey(0)

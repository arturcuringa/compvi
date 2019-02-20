import numpy as np
import cv2

if __name__ == '__main__':
    img = np.zeros((255,255) ,dtype=np.uint8)
    img = np.array([ [i] * row.shape[0] for i,row in enumerate(img)], dtype=np.uint8)
    cv2.imshow('gradient', img)
    cv2.waitKey(0)

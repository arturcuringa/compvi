import numpy as np
import cv2

def vertical_gradient(min_color, max_color, shape)
    ratio = shape
    img = np.array([ [i* ratio] * row.shape[0] for i,row in enumerate(img)], dtype=np.uint8)
if __name__ == '__main__':
    img = np.zeros((100,100) ,dtype=np.uint8)
    ratio = 255 // 100 
    
    cv2.imshow('gradient', img)
    cv2.waitKey(0)

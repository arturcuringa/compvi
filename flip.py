import sys
import cv2

if __name__ == '__main__':
    img_path = sys.argv[1]
    img = cv2.imread(img_path, 1)
    cv2.imshow('flip', cv2.flip(img, 0))
    cv2.waitKey(0)

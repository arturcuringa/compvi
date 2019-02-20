import sys
import cv2


def split_channel(img):
    r = img.copy()
    b = img.copy()
    g = img.copy()
    r[:, :, 1] = 0
    r[:, :, 0] = 0
    g[:, :, 0] = 0
    g[:, :, 2] = 0
    b[:, :, 1] = 0
    b[:, :, 2] = 0

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

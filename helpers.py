import cv2
import numpy as np

def normalize(img):
    # convert to  value gray scale
    img_gray = im2gray(img)

    #smooth to reduce noise a bit more
    gray = cv2.medianBlur(img_gray, 5)

    return img_gray

def radius2value(radius):
    if radius <= 60:
        return "5"
    elif radius <= 65:
        return "1"
    else:
        return "2"


def im2gray(img):
    return  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def imfilter(img, kernel):
    out = cv2.filter2D(img, -1, kernel)
    return out


def imshow(img):
    cv2.imshow("image", img)
    cv2.waitKey(0) 
    cv2.destroyAllWindows() 
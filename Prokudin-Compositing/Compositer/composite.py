#!/bin/python3

import cv2 as cv
import numpy as np
import os

# pull up an image in a new window, removes when ESC is pressed
def show(img):
    cv.imshow('image', img)
    key = cv.waitKey() & 0xFF
    if key == 27:
        cv.destroyAllWindows()

def makeSet(dir):
    imgList = []
    if dir[-1] == '/':
        dir = dir[:-1]
    for a in os.listdir(dir):
        if a[-4:] in ('.jpg', '.png', 'jpeg','gif'):
            imgList.append(cv.imread(dir+'/'+a))
    return imgList

# blue, red, and green are all tuples
# red = (image, y offset, x offset)
def composite(blue, green, red):
    blue, green, red = removeExtra(blue, green, red)
    img = cv.merge((blue, green, red))
    return img


# remove extra is currently returning images that are not the same size
def removeExtra(blue, green, red):
    blue_img, b_y_off, b_x_off = blue
    green_img, g_y_off, g_x_off = green
    red_img, r_y_off, r_x_off = red
    b_y_max, b_x_max = blue_img.shape[:2]
    g_y_max, g_x_max = green_img.shape[:2]
    r_y_max, r_x_max = red_img.shape[:2]
    max_y = min(b_y_max - b_y_off, g_y_max - g_y_off, r_y_max - r_y_off)
    max_x = min(b_x_max - b_x_off, g_x_max - g_x_off, r_x_max - r_x_off)
    blue_img = blue_img[b_y_off : max_y, b_x_off : max_x]
    green_img = green_img[g_y_off : max_y, g_x_off: max_x]
    red_img = red_img[r_y_off : max_y, r_x_off : max_x]
    assert(blue_img.shape[:2] == green_img.shape[:2] and green_img.shape[:2] == red_img.shape[:2])
    return blue_img, green_img, red_img

# takes range and error function, returns y, x offsets that minimize error function
def minimizeError(img_1, img_2, y_min, y_max, x_min, x_max, errorFunct):

    # initial min value is no offset
    err_min = errorFunct(img_1, img_2, 0, 0)
    print('initial error funct is ', err_min)
    err_min_y = 0;
    err_min_x = 0;

    for i in range(y_min, y_max):
        for j in range(x_min, x_max):
            tmp = errorFunct(img_1, img_2, i, j)
            if tmp < err_min:
                err_min = tmp
                err_min_y = i
                err_min_x = j
    return err_min_y, err_min_x

def dumbErrorFunct(img_1, img_2, y, x):

    assert(img_1.shape[:2] == img_2.shape[:2])
    # first align image 2 to image 1 with x and y as offsets
    y_max, x_max = img_1.shape[:2]
    if y < 0 and x < 0:
        img_1 = img_1[0 : y_max + y, 0 : x_max + x]
        img_2 = img_2[-1 * y: , -1 * x : ]
        assert(img_1.shape[:2] == img_2.shape[:2])
    elif y < 0:
        img_1 = img_1[0 : y_max + y, x : ]
        img_2 = img_2[-1 * y: , : x_max - x]
    elif x < 0:
        img_1 = img_1[y : , : x_max + x]
        img_2 = img_2[: y_max - y, -1 * x : ]
    else:
        img_1 = img_1[ y: , x: ]
        img_2 = img_2[ :y_max - y , :x_max - x ]

    assert(img_1.shape[:2] == img_2.shape[:2])

    raw_dif = np.mean(cv.absdiff(img_1, img_2))

    lap_img_1 = cv.Laplacian(cv.GaussianBlur(img_1, (9,9),0), cv.CV_64F, 9)
    lap_img_2 = cv.Laplacian(cv.GaussianBlur(img_2, (9,9),0), cv.CV_64F, 9)

    laplacian_dif = np.mean(cv.absdiff(lap_img_1, lap_img_2))

    return raw_dif * laplacian_dif

testDir = '../data-sets/design-set'
testSet = makeSet(testDir)


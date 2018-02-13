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
    return blue_img, green_img, red_img

# runs a fine gausian kernel over image to smooth, and scales pixels to 
#def clean(img):


testDir = '../data-sets/design-set'
testSet = makeSet(testDir)


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

testDir = '../data-sets/design-set'
testSet = makeSet(testDir)

def testModule():
    for i in testSet:
        show(i)



import cv2
import numpy as np
import composite as c
import formatter as f

def run():
    i = 0
    for e in c.testSet:
        split_group = f.split(e)
        cropped_group = []
        for i in split_group:
            cropped_group.append(f.crop(i))
        print('done cropping')
        blue =  (f.clean(cropped_group[0]), 0, 0)
        green = (f.clean(cropped_group[1]), 0, 0)
        red = (f.clean(cropped_group[2]), 0, 0)
        img = c.composite(blue, green, red)
        #img = cv2.merge((img[0][0:200, 0:200], img[1][0:200, 0:200], img[2][0:200, 0:200]))
        c.show(img)
        img2=cv2.normalize(img,None,0,255,cv2.NORM_MINMAX)
        c.show(img2)


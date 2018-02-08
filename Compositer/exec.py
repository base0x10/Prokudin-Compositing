import cv2
import numpy as np
import composite as c
import formatter as f

for e in c.testSet:
    split_group = f.split(e)
    cropped_group = []
    for i in split_group:
        cropped_group.append(f.crop(i))
    print('done cropping')
    blue =  (cv2.cvtColor(cropped_group[0], cv2.COLOR_BGR2GRAY), 0, 0)
    green = (cv2.cvtColor(cropped_group[1], cv2.COLOR_BGR2GRAY), 0, 0)
    red = (cv2.cvtColor(cropped_group[2], cv2.COLOR_BGR2GRAY), 0, 0)
    img = c.composite(blue, green, red)
    #img = cv2.merge((img[0][0:200, 0:200], img[1][0:200, 0:200], img[2][0:200, 0:200]))
    c.show(img)


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

# runs the core pipeline, going from a raw triple plate image aligned and corrected color image
def processImg(img):
    split_group = f.split(img)
    cropped_group = []
    for i in split_group:
        cropped_group.append(i)
    blue_comp = f.clean(cropped_group[0])
    green_comp = f.clean(cropped_group[1])
    red_comp = f.clean(cropped_group[2])

    assert(blue_comp.shape[:2] == green_comp.shape[:2] and green_comp.shape[:2] == red_comp.shape[:2])

    green_y, green_x = c.minimizeError(blue_comp, green_comp, -10, 11, -10, 11, c.dumbErrorFunct)
    red_y, red_x = c.minimizeError(blue_comp, red_comp, -10, 11, -10, 11, c.dumbErrorFunct)
    print(green_y, green_x)
    print(red_y, red_x)
    blue =  (blue_comp, 0, 0)
    green = (green_comp, green_y, green_x)
    red = (red_comp, red_y, red_x)

    return c.composite(blue, green, red)

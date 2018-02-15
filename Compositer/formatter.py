import cv2
import numpy as np

# takes an image and returns a list of the three split images
def split(img):
    y_max, x_max = img.shape[:2]
    images = []
    first_third = y_max // 3
    second_third = 2*y_max//3
    images.append(img[0 : first_third, : ])
    images.append(img[first_third : second_third, : ])
    images.append(img[second_third :, :])
    for i in range(len(images)):
        images[i] = cv2.cvtColor(images[i][:first_third, :x_max], cv2.COLOR_BGR2GRAY)
    assert(images[0].shape[:2] == images[1].shape[:2] == images[2].shape[:2])
    return images

def crop(img):
    y_max, x_max = img.shape[:2]
    kernel_sz = y_max / 20
    if kernel_sz % 2 == 0:
        kernel_sz = kernel_sz + 1
    median = cv2.medianBlur(img, 9)
    lower_edge = y_max - 5
    upper_edge = 5
    right_edge = x_max - 5
    left_edge = 5
    # cut in on top border
    while upper_edge < y_max / 10 and np.mean(median[ 0 : upper_edge , 0 : x_max ]) > .8 * 255:
        upper_edge = upper_edge + 3
    # cut in bottom border
    while lower_edge > y_max * .9 and np.mean(median[ lower_edge : y_max, 0 : x_max ]) > .8 * 255:
       lower_edge = lower_edge - 3
    # right border
    while right_edge > x_max *.9 and np.mean(median[ 0 : y_max , right_edge : x_max ]) > .8 * 255:
        right_edge = right_edge - 3
    # left border
    while left_edge < x_max *.1 and np.mean(median[ 0 : y_max , 0 : left_edge]) > .8 * 255:
        left_edge = left_edge + 3
    return img[upper_edge : lower_edge , left_edge : right_edge]

def clean(img):
    img = cv2.GaussianBlur(img,(3,3),0)
    return cv2.normalize(img,None,0,255,cv2.NORM_MINMAX)



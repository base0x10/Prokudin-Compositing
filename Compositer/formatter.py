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
    return images

def crop(img):
    median = cv2.medianBlur(img, 7)
    y_max, x_max = median.shape[:2]
    lower_edge = y_max - 5
    upper_edge = 5
    right_edge = x_max - 5
    left_edge = 5
    # cut in on top border
    while np.mean(median[ 0 : upper_edge , 0 : x_max ]) > .8 * 255:
        print(np.sum(median[ 0 : upper_edge , 0 : x_max ]))
        print("upper_edge" + str(upper_edge))
        upper_edge = upper_edge + 1
    # cut in bottom border
    while np.mean(median[ lower_edge : y_max, 0 : x_max ]) > .8 * 255:
        print(np.sum(median[ lower_edge: y_max, 0 : x_max ]))
        print("lower_edge" + str(lower_edge))
        lower_edge = lower_edge - 1
    # right border
    while np.mean(median[ 0 : y_max , right_edge : x_max ]) > .8 * 255:
        right_edge = right_edge - 1
    # left border
    while np.mean(median[ 0 : y_max , 0 : left_edge]) > .8 * 255:
        print(np.mean(median[ 0 : y_max , 0 : left_edge]))
        left_edge = left_edge + 1
    return img[upper_edge : lower_edge , left_edge : right_edge]

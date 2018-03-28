import cv2
import numpy as np
import math

def correlation(patch1, patch2):
    assert(patch1.shape[:2] == patch2.shape[:2])
    standard_dev = patch1.std() * patch2.std()
    mult = (patch1 - patch1.mean()) * (patch2 - patch2.mean())
    if standard_dev == 0:
        return 0
    else:
        return np.mean(mult) / standard_dev

def dist(l_image, r_image, a, b, k_size):
    src_patch = l_image[a:a + k_size, b:b + k_size]

    best_cor = 0
    best_dist = -1;

    i = 0
    while (i < len(r_image) - k_size):
        j = 0
        while (j < len(r_image[0]) - k_size):
            cor = correlation(src_patch, r_image[i:i+k_size, j:j+k_size])
            if cor > best_cor:
                best_cor = cor
                best_dist = np.sqrt(math.pow(a - i,2) + math.pow(b - j,2))
            j = j+k_size
        i = i + k_size

    assert(best_dist > -1)
    return best_dist

def depth(lframe, rframe, k_size = 5):
    l_image = cv2.cvtColor(lframe, cv2.COLOR_BGR2GRAY)
    r_image = cv2.cvtColor(rframe, cv2.COLOR_BGR2GRAY)

    result = l_image[:]
    i = 0
    while (i < len(r_image) - k_size):
        print("at index")
        print(i)
        print("out of:")
        print(len(r_image))
        j = 0
        while( j < len(l_image[0]) - k_size):
            res = dist(l_image, r_image, i, j, k_size)

            result[i][j] = dist(l_image, r_image, i, j, k_size)
            j = j + k_size
        i = i + k_size
    return result

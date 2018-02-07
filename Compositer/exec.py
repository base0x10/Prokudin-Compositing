import cv2
import numpy as np
import composite as c
import formatter as f

list = []
for e in c.testSet:
    for i in f.split(e):
        list.append(i)

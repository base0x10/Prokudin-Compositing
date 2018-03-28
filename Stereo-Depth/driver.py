import numpy as np
import cv2
import skvideo.io
from depth import depth

# image processing example

#limg = cv2.imread("AS15_10325.Panorama_3015x29170.tif")
#rimg = cv2.imread("AS15_10320.Panorama_3015x29170.tif")

limg = cv2.imread("small_left.tif")
rimg = cv2.imread("small_right.tif")

output = depth(limg, rimg, 25)

cv2.imwrite('depth-map.jpg', output)

print("finished...")

# comment this out to continue

exit()
# video processing example

skew = 5
vid = skvideo.io.vread("Eros-Rot.mov")
vid_out = []

for index in range(len(vid) - skew):

    frame = depth(vid[index], vid[index + skew])
    vid_out.append(frame)

    # Display the resulting frame
    # cv2.imshow('frame',frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

# write out the output file
skvideo.io.vwrite("depth-map.mp4", vid_out)

# When everything done, release the capture
cv2.destroyAllWindows()

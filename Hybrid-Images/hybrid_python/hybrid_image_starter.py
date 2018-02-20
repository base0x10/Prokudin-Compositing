import matplotlib.pyplot as plt
import numpy as np
import hybridizer as hy
from align_image_code import align_images
from skimage import color

def toGray(img):
    return color.rgb2gray(img)

def getFFT(img):
    gray_img = toGray(img)
    return np.log(np.abs(np.fft.fftshift(np.fft.fft2(gray_img))))

# First load images

# high sf
im1 = plt.imread('../Images/trump.jpg')/255.

# low sf
im2 = plt.imread('../Images/pennywise.jpg')/255.

# Next align images (this code is provided, but may be improved)
im1_aligned, im2_aligned = align_images(im1, im2)

## You will provide the code below. Sigma1 and sigma2 are arbitrary 
## cutoff values for the high and low frequencies

sigma1 = 1
sigma2 = 45
hybrid = hy.hybrid_image(im1_aligned, im2_aligned, sigma1, sigma2)

plt.imshow(hybrid)
plt.ginput(1)

## Compute and display Gaussian and Laplacian Pyramids
## You also need to supply this function
N = 5 # suggested number of pyramid levels (your choice)
#pyramids(hybrid, N)

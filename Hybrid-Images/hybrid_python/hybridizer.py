import cv2 as cv
import numpy as np
from skimage import color

def toGray(img):
    return color.rgb2gray(img)


# returns a grayscale fft on a log scale for the grayscale of the image passed to it
def getFFT(img):
    gray_img = toGray(img)
    return np.log(np.abs(np.fft.fftshift(np.fft.fft2(gray_img))))

# this is the main function that is called
# image 1 will have large features and color
# image 2 will have small features and no color
def hybrid_image(im1, im2, sigma1, sigma2):

    im2 = highPass(im2, sigma2)
    im2 = toGray(im2)
    im2 = np.divide(im2, 2)
    im2 = cv.merge((im2, im2, im2))

    im1 = lowPass(im1, sigma1)
    #im1 = toGray(im1)
    im1 = np.divide(im1, 2)
    #im1 = cv.merge((im1, im1, im1))

    return cv.add(im2, im1)

# filters out high frequency information
def lowPass(img, sigma):
    return cv.GaussianBlur(img,(sigma, sigma),0)

def highPass(img, sigma):
    blur = lowPass(img, sigma)
    return np.abs(np.subtract( img, blur))

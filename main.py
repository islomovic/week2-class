import cv2
from numpy.ma.core import shape
import matplotlib.pyplot as plt

#
# cv2.imshow("new image", img)
# shape = img.shape
# print(shape)
# print("height of image ", int(img.shape[0]), "pixels")
# print ('Width of Image: ', int(img.shape[1]), 'pixels')


# img = cv2.imread('image.jpg')
# img[200:500,300:600,:] = 255
# plt.imshow(img[...,::-1])
#

# image = cv2.imread('image.jpg')
# cv2.imshow('Original', image)
# cv2.waitKey()
#
#
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# cv2.imshow('Grayscale', gray_image)
# cv2.waitKey()
# cv2.destroyAllWindows()


# GRAYYYYYYY
#
# import cv2
# import matplotlib.pyplot as plt
#
# img = cv2.imread('image.jpg')
#
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.title("Image")
# plt.axis("off")
#
# print("Shape:", img.shape)
#
# B, G, R = img[10, 50]
# print("B:", B, "G:", G, "R:", R)
#

# 03

import cv2
import numpy as np
import matplotlib.pyplot as plt

# image = cv2.imread('image.jpg')
# plt.imshow(image[...,::-1])
#
# height, width = image.shape[:2]
#
#
# cropped = image[150:300 , 150:650]
#
# plt.imshow(cropped[...,::-1])
# cv2.imshow("original", image)
# cv2.imshow("cropped", cropped)
#
# cv2.waitKey()
# cv2.destroyAllWindows()
#


# 4  color spaces

# img = cv2.imread('image.jpg')
# hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
# cv2.imshow('Original', img)
# cv2.imshow('HSV image', hsv_image)
# cv2.imshow('Hue channel', hsv_image[:, :, 0])
# cv2.imshow('Saturation channel', hsv_image[:, :, 1])
# cv2.imshow('Value channel', hsv_image[:, :, 2])
#
#
#
# cv2.waitKey()
# cv2.destroyAllWindows()

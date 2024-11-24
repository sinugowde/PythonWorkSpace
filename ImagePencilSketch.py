# pip install opencv-python
import cv2
from matplotlib import pyplot as plt
import time

colored_pict = False

# image = cv2.imread("IMG_20160819_110916.jpg")
image = cv2.imread("IMG_20160417_104042.jpg")
resized_image = cv2.resize(image, (800, 800))  # Resize to 400x400
cv2.imshow('Image', resized_image)
cv2.waitKey(0)

if colored_pict:
    gray_image = resized_image
else:
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Image', gray_image)
cv2.waitKey(0)

inverted = 255-gray_image
cv2.imshow('Image', inverted)
cv2.waitKey(0)

blur = cv2.GaussianBlur(inverted, (21, 21), 0)
invertedblur = 255-blur

cv2.imshow('Image', invertedblur)
cv2.waitKey(0)

sketch = cv2.divide(gray_image, invertedblur, scale=256.0)
cv2.imwrite("sketch_image1.png", sketch)
cv2.imshow("Image", sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()

# img = cv2.imread('IMG_20160819_110916.jpg')
# plt.imshow(img, cmap = 'winter', interpolation = 'spline36')
# # plt.imshow(img, cmap = 'rgb')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()
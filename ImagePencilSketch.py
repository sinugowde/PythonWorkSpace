# pip install opencv-contrib-python
import cv2
from matplotlib import pyplot as plt
import time

# Change this value to True or False for switch between Color & Balck&White
colored_pict = True

def resize_image(image_path, max_size=800):

  img = cv2.imread(image_path)

  # Get the image dimensions
  height, width, _ = img.shape

  # Calculate the scaling factor
  scale_factor = min(max_size / width, max_size / height)

  # Resize the image

  resized_img = cv2.resize(img, None, fx=scale_factor, fy=scale_factor)

  return resized_img


# image_path = 'Images/IMG_20160417_104042.jpg'
image_path = 'Images/roses.jpg'

# image = cv2.imread("Images/roses.jpg")
resized_image = resize_image(image_path)

# resized_image = cv2.resize(image, (800, 800))  # Resize to 400x400
# cv2.imshow('Image Window1', resized_image)
cv2.imshow('Image Window1', resized_image)
cv2.waitKey(0)

if colored_pict:
    gray_image = resized_image
else:
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Image Window2', gray_image)
cv2.waitKey(0)

inverted = 255-gray_image
cv2.imshow('Image Window3', inverted)
cv2.waitKey(0)

blur = cv2.GaussianBlur(inverted, (21, 21), 0)
invertedblur = 255-blur

cv2.imshow('Image Window4', invertedblur)
cv2.waitKey(0)

sketch = cv2.divide(gray_image, invertedblur, scale=256.0)
cv2.imwrite("sketch_image1.png", sketch)
cv2.imshow('Image Window5', sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()

# img = cv2.imread('IMG_20160819_110916.jpg')
# plt.imshow(img, cmap = 'winter', interpolation = 'spline36')
# # plt.imshow(img, cmap = 'rgb')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()
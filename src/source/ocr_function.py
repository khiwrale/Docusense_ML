#!/usr/bin/env python
# coding: utf-8

import cv2
# from google.colab.patches import cv2_imshow
import numpy as np
import matplotlib.pyplot as plt
import os

image_path = 'C:/Docusense-ML/src/data/Image/Img_Tilt/tilt7.png'
img = cv2.imread(image_path)

class OCR_ImagePreprocessing():
  def display_image_in_actual_size(self,im_path):
    dpi = 80
    im_data = plt.imread(im_path)
    height, width, depth = im_data.shape

    # What size does the figure need to be in inches to fit the image?
    figsize = width / float(dpi), height / float(dpi)

    # Create a figure of the right size with one axes that takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    # Hide spines, ticks, etc.
    ax.axis('off')

    # Display the image.
    ax.imshow(im_data, cmap='gray')

    plt.show()

  def inverted_image(self, image):
    inv_img = cv2.bitwise_not(img)
    return cv2_imshow(inv_img)

  # def rescaling(self):

  # Binarization
  def grayscale(self, image):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY )
    return cv2_imshow(gray_img)
 
  # Method 1
  def adjusting_black_white(self, image):
    thresh, bw_img = cv2.threshold(gray_img, 128,255, cv2.THRESH_BINARY)
    return cv2_imshow(bw_img)

  # Method 2
  def adaptiveThreshold(self, image):
    adap_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2) 
    return cv2_imshow(adap_img)

  def noise_removal(self, image):
    # kernel = np.ones((1,1), np.uint8)
    # image = cv2.dilate(image, kernel, iterations = 1)
    # kernel = np.ones((1,1), np.uint8)
    # image = cv2.erode(image, kernel, iterations = 1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return cv2_imshow(image)

  def thin_font (self, image):
    kernel = np.ones((1,1), np.uint8)
    erod_img = cv2.erode(image, kernel, iterations = 1)
    return cv2_imshow(erod_img)

  def thick_font (self, image):
    kernel = np.ones((1,1), np.uint8)
    dilation_img = cv2.dilate(image, kernel, iterations = 1)
    return cv2_imshow(dilation_img)

  def remove_border(self, image):
    contours, heiarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntsSorted = sorted(contours, key= lambda x:cv2.contourArea(x))
    cnt = cntsSorted[-1]
    x, y, w, h = cv2.boundingRect(cnt)
    crop = image[y:y + h, x:x + w]
    return cv2_imshow(crop)

  def missing_borders(self, image):
    color = [255, 255, 255]
    top, bottom, left, right = [150] * 4
    image_with_border = cv2.copyMakeBorder(no_noise, top, bottom, left, right, cv2.BORDER_CONSTANT, value = color)
    return cv2_imshow(image_with_border)

  def getSkewAngle(cvImage) -> float:
    # Prep image, copy, convert to gray scale, blur, and threshold
    newImage = cvImage.copy()
    gray = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Apply dilate to merge text into meaningful lines/paragraphs.
    # Use larger kernel on X axis to merge characters into single line, cancelling out any spaces.
    # But use smaller kernel on Y axis to separate between different blocks of text
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=5)

    # Find all contours
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)

    # Find largest contour and surround in min area box
    largestContour = contours[0]
    minAreaRect = cv2.minAreaRect(largestContour)

    # Determine the angle. Convert it to the value that was originally used to obtain skewed image
    angle = minAreaRect[-1]
    if angle < -45:
        angle = 90 + angle
    return -1.0 * angle


    # Rotate the image around its center
  def rotateImage(cvImage, angle: float):
      newImage = cvImage.copy()
      (h, w) = newImage.shape[:2]
      center = (w // 2, h // 2)
      M = cv2.getRotationMatrix2D(center, angle, 1.0)
      newImage = cv2.warpAffine(newImage, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
      return newImage
      
    # Deskew image
  def deskew(cvImage):
    angle = getSkewAngle(cvImage)
    return rotateImage(cvImage, -1.0 * angle)
  # def transparency_or_ AlphaChannel(self, image):

OCR_PP = OCR_ImagePreprocessing()
OCR_PP.display_image_in_actual_size(image_path)
OCR_PP.inverted_image(img)
OCR_PP.grayscale(img)
# OCR_PP.adjusting_black_white(gray_img)
# OCR_PP.adaptiveThreshold(gray_img)
# OCR_PP.noise_removal(gray_img)
# OCR_PP.thin_font(gray_img)
# OCR_PP.thick_font(gray_img)
# OCR_PP.remove_border(gray_img)
# OCR_PP.missing_borders(image)


### Step 8: >>> 6. Rotation or Deskewing <<<<<<<<<<<<<<<<<<<<<<<<<<

image_path = 'C:/Docusense-ML/src/data/Image/Img_Tilt/tilt7.png'
img = cv2.imread(image_path)
# cv2_imshow(img)


folder = os.listdir("C:/Docusense-ML/src/data/Image/Img_Tilt")

for file in folder:
  folder_path = "C:/Docusense-ML/src/data/Image/Img_Tilt/"
  img = cv2.imread(folder_path + file)
  # print(cv2_imshow(img))



  fixed = deskew(img)
  cv2.imwrite(f"C:/Docusense-ML/src/data/output_{file}", fixed)
  print("-------------------------------------------------")
  print(getSkewAngle(img))

  cv2_imshow(cv2.imread(f"C:/Docusense-ML/src/data/output_{file}"))

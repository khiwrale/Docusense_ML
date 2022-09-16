#!/usr/bin/env python
# coding: utf-8

import cv2
import imutils

import matplotlib
import matplotlib.pyplot as plt

import numpy as np

from scipy import stats
from scipy import ndimage

from skimage.transform import (hough_line, hough_line_peaks)
from skimage.feature import canny
from skimage.measure import label   


def image_tilt_correction():

    img=cv2.imread('C:\Docusense-ML\src\data\Image\Img_Tilt\Rotated.png')

    img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #simple threshold
    ret,thresh_img = cv2.threshold(img_grey,100,255,cv2.THRESH_BINARY)

    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((3,30), np.uint8)
    img_dilation = cv2.dilate(thresh_img, kernel, iterations=1)
    img_erosion = cv2.erode(thresh_img, kernel, iterations=1)

    # #find contours
    contours, hierarchy = cv2.findContours(img_erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # #create an empty image for contours
    img_contours = np.zeros(img.shape)

    # draw the contours on the empty image
    cv2.drawContours(img_contours, contours, -1, (0,255,0), 1)
    matplotlib.rcParams["figure.dpi"] = 300
    plt.imshow(img_contours)
    plt.savefig('img_contours.png',dpi=300, bbox_inches='tight')

    # Perform Hough Transformation to detect lines
    hspace, angles, distances = hough_line(img_contours[:,:,1])

    # Find angle

    angle=[]
    for _, a , distances in zip(*hough_line_peaks(hspace, angles, distances)):
        angle.append(a)


    labels = label(img_contours[:,:,1])
    assert( labels.max() != 0 ) # assume at least 1 CC
    largestCC = labels == np.argmax(np.bincount(labels.flat)[1:])+1


    img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = canny(img_grey)


    #tested_angles = np.linspace(-np.pi / 2, np.pi / 2, 360, endpoint=False)
    tested_angles = np.deg2rad(np.arange(0.1, 180.0))
    h, theta, d = hough_line(largestCC, theta=tested_angles)

    # find line peaks and angles
    accum, angles, dists = hough_line_peaks(h, theta, d)

    # round the angles to 2 decimal places and find the most common angle.
    most_common_angle = stats.mode(np.around(angles, decimals=2))[0]

    # convert the angle to degree for rotation.
    skew_angle = np.rad2deg(most_common_angle - np.pi/2)

    # rotate image according to skew_angle

    #img_corrected = ndimage.rotate(img_grey, skew_angle, mode = 'mirror')
    output1_image = imutils.rotate(img, int(skew_angle)+92)


    fig, axs = plt.subplots(2)
    fig.set_dpi(300.0)

    axs[0].imshow(img)
    axs[1].imshow(output1_image)

    #plt.savefig('output.png', dpi=500, bbox_inches='tight')

# skew_angle
image_tilt_correction()
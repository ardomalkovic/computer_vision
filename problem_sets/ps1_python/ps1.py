#!/usr/bin/env python

import cv2
import numpy as np
import matplotlib.pyplot as plt

# ps1

# 1-a
#img = imread(fullfile('input', 'ps1-input0.png'));  % already grayscale
# TODO: Compute edge image img_edges
#imwrite(img_edges, fullfile('output', 'ps1-1-a-1.png'));  % save as output/ps1-1-a-1.png

# 2-a
#[H, theta, rho] = hough_lines_acc(img_edges);  % defined in hough_lines_acc.m
# TODO: Plot/show accumulator array H, save as output/ps1-2-a-1.png

#%% 2-b
#peaks = hough_peaks(H, 10);  % defined in hough_peaks.m
#%% TODO: Highlight peak locations on accumulator array, save as output/ps1-2-b-1.png

#%% TODO: Rest of your code here
'''
Load the input grayscale image (input/ps1-input0.png) as img and generate an
edge image – which is a binary image with white pixels (1) on the edges and
black pixels (0) elsewhere.

For reference, do “doc edge” in Matlab and read about edge operators. Use 
one operator of your choosing – for this image it probably won’t matter much.
If your edge operator uses parameters (like ‘canny’) play with those until
you get the edges you would expect to see.
'''
img1 = cv2.imread('input/ps1-input0.png', 0)

plt.imshow(img1, cmap="gray")

plt.show()

import numpy as np
import matplotlib.pyplot as plt
import cv2
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def shift_left_and_right(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blured = cv2.GaussianBlur(img_gray, (71, 71), 0)

    plt.imshow(img_blured, cmap="gray")
    img_left = np.copy(img_blured)
    img_right = np.copy(img_blured)
    img_left[:, :-1] = img_blured[:, 1:]
    img_right[:, 1:] = img_blured[:, :-1]
    my_edge = img_left - img_right
    return my_edge


def auto_canny(image, sigma=0):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # compute the median of the single channel pixel intensities
    v = np.median(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper,L2gradient=False)

    # return the edged image
    return edged


def laplasian_of_gaussian(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (21, 21), 0)
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    return laplacian

img = cv2.imread("data/20170612_233329.jpg")
#img = cv2.imread("data/ada_nerdzik.jpg")


edged = shift_left_and_right(img)
canny_edge = auto_canny(img)
log = laplasian_of_gaussian(img)
plt.imshow(log, cmap="gray")

plt.show()

import numpy as np
import matplotlib.pyplot as plt
import cv2

from math_operations import cross_correlation
from filters import gaussian_filter, sobel_filters


def shift_left_and_right(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blured = cv2.GaussianBlur(img_gray, (5, 5), 0)

    plt.imshow(img_blured, cmap="gray")
    img_left = np.copy(img_blured)
    img_right = np.copy(img_blured)
    img_left[:, :-1] = img_blured[:, 1:]
    img_right[:, 1:] = img_blured[:, :-1]
    my_edge = img_left - img_right

    return img_blured


def auto_canny(image, sigma=0):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # compute the median of the single channel pixel intensities
    v = np.median(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper, L2gradient=False)

    # return the edged image
    return edged


def own_canny(image, sigma=0):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # compute the median of the single channel pixel intensities
    # v = np.median(image)

    # apply automatic Canny edge detection using the computed median
    # lower = int(max(0, (1.0 - sigma) * v))
    # upper = int(min(255, (1.0 + sigma) * v))

    #create gaussian filter
    sigma = np.array([[1, 0], [0, 1]])
    gaussian = gaussian_filter(1, sigma)

    #calculate gauusian deritive for fatser computation
    Sx, Sy = sobel_filters()
    aa =  np.array([[1, 2, 3],
                    [1, 2, 3],
                    [1, 2, 3],
                    [1, 2, 3],
                    [1, 2, 3]
                    ])
    bb = cross_correlation(aa, Sx)
    cc = cross_correlation(aa, Sx)
    print(bb)
    print(cc)
    exit()
    d_x = cross_correlation(gaussian, Sx)
    d_y = cross_correlation(gaussian, Sy)
    abs_d_x = cv2.convertScaleAbs(d_x)
    abs_d_y = cv2.convertScaleAbs(d_y)
    grad = cv2.addWeighted(abs_d_x, 0.5, abs_d_y, 0.5, 0)
    print(grad.shape)

    #apply gussian filter for blure image
    edged = cross_correlation(image, grad)

    # return the edged image
    return edged


def laplasian_of_gaussian(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (21, 21), 0)
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    return laplacian


img = cv2.imread("zhufor.jpg")

edged = shift_left_and_right(img)
print(edged.shape)
canny_edge = own_canny(img)
log = laplasian_of_gaussian(img)
plt.imshow(canny_edge, cmap="gray")

plt.show()

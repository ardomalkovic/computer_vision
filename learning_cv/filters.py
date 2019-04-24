import numpy as np
from math_operations import cross_correlation, multivariate_gaussian
import cv2
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


def laplacian_filters():
    lap = np.array([[ 0, -1,  0],
                    [-1,  4, -1],
                    [ 0, -1,  0]])
    diag_lap = np.array([[-1, -1, -1],
                         [-1,  8, -1],
                         [-1, -1, -1]])
    return lap, diag_lap


def sobel_filters():
    Gy = np.array([[-1, -2, -1],
                   [ 0,  0,  0],
                   [ 1,  2,  1]])
    return Gy.T, Gy


def gaussian_filter(half_size, sigma):
    """Retun the Gaussian filter with dimensions: 
    (2*half_size+1, 2*half_size+1), and simga from input)

    Inputs:
        half_size: int
        sigma: np.array shape [n,n]
    Outputs:
        np.array with gaussian values
    """
    x, y = np.meshgrid(np.linspace(-half_size, half_size, 2*(half_size)+1),
                       np.linspace(-half_size, half_size, 2*(half_size)+1))

    domain = np.empty(x.shape + (2,))
    domain[:, :, 0] = x
    domain[:, :, 1] = y

    return multivariate_gaussian(domain, np.array([0, 0]), sigma)


#TEST SOBELA
# img = np.array([[0.0, 0.0, 0.0, 0.0, 0.0],
                # [0.1, 0.1, 0.1, 0.1, 0.1],
                # [0.2, 0.2, 0.2, 0.2, 0.2],
                # [0.3, 0.3, 0.3, 0.3, 0.3],
                # [0.4, 0.4, 0.4, 0.4, 0.4]])
# print(img)
# Gx, Gy = sobel_filters()
# sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
# sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
# print(sobely)
# print(cross_correlation(img, Gy))

# TEST GAUSIAN FILTER
# half_size = 1
# sigma = np.array([[1, 0], [0, 1]])
# x, y = np.meshgrid(np.linspace(-half_size, half_size, 2*(half_size)+1),
                   # np.linspace(-half_size, half_size, 2*(half_size)+1))

# pos = np.empty(x.shape + (2,))
# pos[:, :, 0] = x
# pos[:, :, 1] = y
# rv = multivariate_normal([0, 0], sigma)
# rv
# plt.contourf(x, y, rv.pdf(pos))
# plt.show()

# print(rv.pdf(pos))
# print(gaussian_filter(half_size, sigma))

# fig = plt.figure()
# ax = fig.gca(projection='3d')

# # Plot the surface.
# surf = ax.plot_surface(x, y, rv.pdf(pos), cmap=cm.coolwarm,
                       # linewidth=0, antialiased=False)

# # Customize the z axis.
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# # Add a color bar which maps values to colors.
# fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

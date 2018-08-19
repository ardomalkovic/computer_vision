import numpy as np
import matplotlib.pyplot as plt
import cv2
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def gaussian_blur(img, half_size, sigma):
    x, y = np.meshgrid(np.linspace(-half_size, half_size, 2*(half_size+1)),
                       np.linspace(-half_size, half_size, 2*(half_size+1)))

    domain = np.empty(x.shape + (2,))
    domain[:, :, 0] = x
    domain[:, :, 1] = y
    gaussian_values = multivariate_gaussian(domain, np.array([0,0]), np.array([[3, 0], [0,3]]))



def multivariate_gaussian(domain, mu, sigma=1):
    """Return the multivariate Gaussian distribution on array domain.
    domain is an array constructed by packing the meshed arrays of variables
    x_1, x_2, x_3, ..., x_k into its _last_ dimension.
    Inputs:
        domain: np.array  meshgrid packing in array: [:, :, 0] = X,
                                                     [:, :, 1] = Y,
        mu: np.array shape [n]
        sigma: np.array shape [n,n]
    Outputs:
        np.array with gaussian values for domain arguments
    """
    n = mu.shape[0]
    Sigma_det = np.linalg.det(sigma)
    Sigma_inv = np.linalg.inv(sigma)
    N = np.sqrt((2*np.pi)**n * Sigma_det)
    # This einsum call calculates (x-mu)T.Sigma-1.(x-mu) in a vectorized
    # way across all the input variables.
    fac = np.einsum('...k,kl,...l->...', domain - mu, Sigma_inv, domain - mu)

    return np.exp(-fac / 2) / N


half_size = 3
x, y = np.meshgrid(np.linspace(-half_size, half_size, 2*half_size+1),
                   np.linspace(-half_size, half_size, 2*half_size+1))

domain = np.empty(x.shape + (2,))
domain[:, :, 0] = x
domain[:, :, 1] = y
aa = multivariate_gaussian(domain, np.array([0,0]), np.array([[3, 0], [0,3]]))
print(aa)

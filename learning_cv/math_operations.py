import numpy as np
from scipy import signal
from scipy import misc


def cross_correlation(matrix, kernel):
    """Implementation cross corelation with same size image output,
    and use copy edge for boundary issues
    Inputs:
        matrix: np.array
        kernel: np array [odd, odd]
    Outputs:
        np.array with cross correlationed values
    """
    edge_size = kernel.shape[0] // 2

    out = np.append(np.flip(matrix[:, :edge_size:], 1), matrix, axis=1)
    out = np.append(out, np.flip(matrix[:, -edge_size:], 1), axis=1)
    out = np.append(np.flip(out[:edge_size, :], 0), out,  axis=0)
    out = np.append(out, np.flip(out[-edge_size:, :], 0),  axis=0)

    out2 = np.empty_like(out)
    for i in range(edge_size, out.shape[0]-edge_size):
        for j in range(edge_size, out.shape[1]-edge_size):
            aa = out[i-edge_size:i+(edge_size+1),
                     j-edge_size:j+(edge_size+1)]
            out2[i][j] = (kernel * aa).sum()

    return out2[edge_size:-edge_size, edge_size:-edge_size]


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


#TEST cross correlation
# img = np.array([[0.0, 0.0, 0.0, 0.0, 0.0],
                # [0.1, 0.1, 0.1, 0.1, 0.1],
                # [0.2, 0.2, 0.2, 0.2, 0.2],
                # [0.3, 0.3, 0.3, 0.3, 0.3],
                # [0.4, 0.4, 0.4, 0.4, 0.4]])
# Sy = np.array([[-1, -2, -1],
               # [ 0,  0,  0],
               # [ 1,  2,  1]])

# own_corr = cross_correlation(img, Sy)
# corr = signal.correlate2d(img, Sy, boundary='symm', mode='same')
# diff = own_corr - corr
# diff = np.around(diff, decimals=1)
# print(np.array_equal(diff, np.zeros_like(diff)))

# print(diff)
# print(np.zeros_like(own_corr))

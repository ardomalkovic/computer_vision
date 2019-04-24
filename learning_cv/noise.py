import numpy as np
import matplotlib.pyplot as plt
import cv2


def gaussian_noise(img):
    sigma = 0.1 * 250
    mu = 127
    noise = (np.random.randn(*img.shape)) * sigma + mu
    print(noise)
    return noise


def s_p_noise(img):
    flat_img = np.reshape(img, -1)
    s_p_place = np.random.randint(flat_img.shape[0],
                                  size=int(0.01*(flat_img.shape[0])))

    salt_place = s_p_place[:int(s_p_place.shape[0]/2)]
    papper_place = s_p_place[int(s_p_place.shape[0]/2)+1:]

    flat_img[salt_place] = 255
    flat_img[papper_place] = 0

    return img

import numpy as np
import matplotlib.pyplot as plt
import cv2
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def gaussian_noise(img):
    sigma = 0.1 * 250
    mu = 127
    noise = (np.random.randn(*img.shape)) * sigma + mu
    print(noise)
    return noise


def s_p_noise(img):

    flat_img = np.reshape(img, -1)
    s_p_place = np.random.randint(flat_img.shape[0], size=int(0.01*(flat_img.shape[0])))

    salt_place = s_p_place[:int(s_p_place.shape[0]/2)]
    papper_place = s_p_place[int(s_p_place.shape[0]/2)+1:]

    flat_img[salt_place] = 255
    flat_img[papper_place] = 0

    return img



# img = read_image("data/20170612_233329.jpg")
img = cv2.imread("data/ada_nerdzik.jpg")


R = img[:, :, 0]
G = img[:, :, 1]
B = img[:, :, 2]


img = 0.299*R + 0.587*G + 0.114*B
img = img.astype(np.uint8)
# print(img.dtype)
s_p = gaussian_noise(img)
# print(s_p)
# noise = add_noise(img)
# print(noise)
# noised = (img + noise).astype(np.uint8)
# noised = (img + s_p).astype(np.uint8)
# print(noised.dtype)
plt.imshow(s_p, cmap="gray")

plt.show()



aa = np.array([[1, 1, 1], [2, 2, 2]])
bb = np.reshape(aa, -1)
bb[3]=4
print(bb.shape)

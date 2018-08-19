import numpy as np
import matplotlib.pyplot as plt
import cv2
# from scipy import signal
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def show_real_image(img):
    R = img[:, :, 0]
    G = img[:, :, 1]
    B = img[:, :, 2]

    img_grey = 0.299*R + 0.587*G + 0.114*B
    # img_grey = img_grey.astype(np.uint8)
    height = img.shape[0]
    width = img.shape[1]
    X, Y = np.meshgrid(np.linspace(0, width,  width), np.linspace(0, -height, height))
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(X, Y, img_grey, cmap=cm.coolwarm)
    plt.show()


def read_image(img_path):
    img = cv2.imread(img_path)
    return img


# img = read_image("data/20170612_233329.jpg")
img = read_image("data/ada_nerdzik.jpg")


show_real_image(img)

print(img.shape)

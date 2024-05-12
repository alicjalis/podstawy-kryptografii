import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
plt.rc('figure', dpi=105)
FONT = cv.FONT_HERSHEY_SIMPLEX
img = np.ones((100, 100), dtype=np.uint8)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, ':)', (40, 55), font, 0.9, (0,0,0), 2)
img = img.astype(bool)
plt.imshow(img, cmap='gray')
plt.show()


def split_shares(img):

    W, H = img.shape
    s1, s2 = np.zeros((2, H, W, 2))
    mask = np.random.rand(H, W) > 0.5

    s1[(img == 1) & (mask == 0)] = [1, 0]
    s2[(img == 1) & (mask == 0)] = [1, 0]

    s1[(img == 1) & (mask == 1)] = [0, 1]
    s2[(img == 1) & (mask == 1)] = [0, 1]

    s1[(img == 0) & (mask == 0)] = [1, 0]
    s2[(img == 0) & (mask == 0)] = [0, 1]

    s1[(img == 0) & (mask == 1)] = [0, 1]
    s2[(img == 0) & (mask == 1)] = [1, 0]

    s1 = s1.reshape(H, 2 * W).astype(bool)
    s2 = s2.reshape(H, 2 * W).astype(bool)
    return s1, s2


def join_shares(x, y):

    # operacja AND na pikselach
    return x == y


s1, s2 = split_shares(img)
z = join_shares(s1, s2)

fig, (ax1,ax2,ax3) = plt.subplots(nrows=3, figsize=(6, 10))
ax1.imshow(s1, cmap='gray')
ax2.imshow(s2, cmap='gray')
ax3.imshow(z, cmap='gray')
plt.show()

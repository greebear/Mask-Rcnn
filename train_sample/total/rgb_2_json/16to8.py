import cv2
import numpy as np
import PIL.Image as Image
from matplotlib import pyplot


im = cv2.imread('label.png', -1)
print('label.png shape :', im.shape)
im = im.astype(np.uint8)
print('label.png shape after astype :', im.shape)
print('label.png shape after astype :', im.dtype)
cv2.imwrite('uint8_label.png', im)
uint8_label = cv2.imread('uint8_label.png', -1)
print('uint8_label.png shape', uint8_label.shape)
print('uint8_label.png dtype', uint8_label.dtype)
res = cv2.resize(uint8_label, (1024, 1024),interpolation=cv2.INTER_CUBIC)
uint8_label = 255/3*uint8_label
pyplot.imshow(uint8_label)
pyplot.show()
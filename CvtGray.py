import cv2
import numpy as np
import os

input_dir = r'C:/Users/zx/Desktop/photo1'
output_dir = r'C:/Users/zx/Desktop/photo2'
for i in range(170, 171):
    lenna = cv2.imread(r'C:/Users/zx/Desktop/photo1/%d.jpg' % i)
    row, col, channel = lenna.shape
    lenna_gray = np.zeros((row, col))
    output_path = os.path.join(output_dir, "%d.jpg" % i)
    for r in range(row):
        for l in range(col):
            lenna_gray[r, l] = 1 / 3 * lenna[r, l, 0] + 1 / 3 * lenna[r, l, 1] + 1 / 3 * lenna[r, l, 2]
    cv2.imshow("lenna_gray", lenna_gray.astype("uint8"))
    cv2.imwrite(output_path, lenna_gray)

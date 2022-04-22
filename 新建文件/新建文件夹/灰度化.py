import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("lenna.png", cv.IMREAD_COLOR)  # 读取指定位置的彩色图像
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("img", gray)  # 显示图片
cv.waitKey(0)  # 等待键盘触发事件，释放窗口

height, width, channel = img.shape

# 分量法
R = np.zeros(img.shape, np.uint8)
G = np.zeros(img.shape, np.uint8)
B = np.zeros(img.shape, np.uint8)
for i in range(height):
    for j in range(width):
        R[i, j] = img[i, j, 0]
        G[i, j] = img[i, j, 1]
        B[i, j] = img[i, j, 2]



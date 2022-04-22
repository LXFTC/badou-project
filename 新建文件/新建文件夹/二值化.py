import cv2 as cv
import numpy as np


def threshold_demo(image):                          #全局阈值
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY|cv.THRESH_OTSU)
    print("threshold value %s"%ret)
    cv.imshow("global_threshold_binary", binary)

def local_threshold(image):                       #局部阈值
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow("local_threshold_binary", binary)


def custom_threshold(image):        #自定义阈值
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]
    m = np.reshape(gray, [1, w*h])  #降维
    mean = m.sum() / (w*h)    #求均值
   # print("mean : ", mean)
    ret, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)#利用均值进行图像二值化
    cv.imshow("custom_threshold_binary", binary)



src = cv.imread("lenna.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
threshold_demo(src)
local_threshold(src)
custom_threshold(src)

cv.waitKey(0)

cv.destroyAllWindows()


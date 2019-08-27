# RGB色彩空间 RGB三个颜色取值（0~255）可形成一个三维空间（立方体）
# color space(锥状空间)
# HSV（柱状空间 ）360 180 180可以进行归一化等操作转化为HSV
import cv2 as cv
import numpy as np

def extract_object():
    capture = cv.VideoCapture('D:/DOC/python Opencv learning/test.mp4')
    while True:
        ret, frame = capture.read()  # ret是读取函数的返回值，若读到最后一帧读不出来了就返回False
        if ret == False:  # 如果返回值是False
            print("read video fail")
            break;
        # convert to hsv
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        # 仅将蓝色的区域提取出来
        lower_hsv = np.array([100, 43, 46])  # 蓝色的低值
        upper_hsv = np.array([124, 255, 255])  # 蓝色的高值
        mask = cv.inRange(hsv,
                   lowerb=lower_hsv,
                   upperb=upper_hsv)  # src, 低值， 高值
        dst = cv.bitwise_and(frame, frame , mask=mask)  # 通过按位与
        cv.imshow('Video', frame)
        cv.imshow('Mask', dst)
        print("show video captures")
        c = cv.waitKey(40)
        if c == 27:  # 27->ESC
            break;


def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # BGR转换为灰度
    cv.imshow("gray", gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)  # BGR转换为HSV
    cv.imshow("hsv", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv",yuv)


# 自己写的，压缩图像倍数的函数
def compression(image):
    n = 10  # 压缩倍数
    [hight, width, layer] = image.shape
    image1 = cv.resize(image, (int(hight / (n/2.25)), int(width / n)))  # 压缩
    cv.imshow("output image", image1)
    return image1

# 读取图片并显示


src1 = cv.imread(r'D:\DOC\python Opencv learning\test.jpg')  # 读图片
# src = compression(src1)
# srcVideo = 'D:/DOC/python Opencv learning/test.mp4'
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src1)  # 通过 OPENCV的GUI显示图像
color_space_demo(src1)
extract_object()
b, g, r = cv.split(src1)
cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)
src1[:, :, 2] = 0  # 将第3个通道改为0
src1 = cv.merge([b, g, r])
cv.imshow("change", src1)
cv.waitKey(0)  # 等待一个按键q输入后退出

cv.destroyAllWindows()  # 关闭所有窗口

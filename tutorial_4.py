import cv2 as cv
import numpy as np
# 像素运算 ：加减乘除->调整亮度和对比度
# 逻辑运算 ：与或非 ->遮罩层控制
# 常见图像混合 算法运算与几何运算


def add_demo(m1, m2):  # 将两个图片叠加起来
    dst = cv.add(m1, m2)
    cv.imshow("add demo", dst)


def subtract(m1, m2):
    dst = cv.subtract(m1, m2)
    cv.imshow("subtract demo", dst)


def divide(m1, m2):
    dst = cv.divide(m1, m2)
    cv.imshow("divide demo", dst)


def multiply(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow("multiply demo", dst)


def others1(m1, m2):
    m1_mean = cv.mean(m1)
    print(m1_mean)
    m2_gray = cv.cvtColor(m2, cv.COLOR_RGB2GRAY)
    m2_equ = cv.equalizeHist(m2_gray)
    cv.imshow("equalizeHist", m2_equ)


def others2(m1, m2):
    mean1, dev1 = cv.meanStdDev(m1)
    mean2, dev2 = cv.meanStdDev(m2)
    h, w = m1.shape[:2]
    print("mean1:", mean1, "\nmean2:", mean2, "\ndev1:", dev1, "\ndev2:", dev2)
    img = np.zeros([h, w], np.uint8)  # 纯色图的方差和均值都是0
    m, dev = cv.meanStdDev(img)
    print("\nm:", m, "\ndev:", dev)

# 逻辑运算


def logic_demo(m1, m2):
    dst = cv.bitwise_and(m1, m2) # 两个图片相与，可以做出字体边框的其他图片等等
    dst1 = cv.bitwise_or(m1, m2)
    dst2 = cv.bitwise_not(m1)
    cv.imshow("logic and", dst)
    cv.imshow("logic or", dst1)
    cv.imshow("logic not", dst2)


def contrast_brightness(image, c, b):  # 源文件/对比度/亮度
    # 扩大像素之间的对比度
    h, w, ch = image.shape
    blank = np.zeros([h, w, ch], image.dtype)  # 长/宽/通道
    dst = cv.addWeighted(image, c, blank, 1-c, b)
    cv.imshow("addWeighted", dst)


src1 = cv.imread(r'D:\DOC\python Opencv learning\test.jpg')  # 读图片
src2 = cv.imread(r'D:\DOC\python Opencv learning\test2.jpg')  # 读图片
print("src1 shape:", src1.shape)
print("src2 shape:", src2.shape)
# cv.namedWindow('input image 1', cv.WINDOW_AUTOSIZE)
cv.imshow("input image 1", src1)  # 通过opcv的GUI显示图像
cv.imshow("input image 2", src2)  # 通过opcv的GUI显示图像
add_demo(src1, src2)
subtract(src1, src2)
divide(src1, src2)
others1(src1, src2)
others2(src1, src2)
multiply(src1, src2)
logic_demo(src1, src2)
contrast_brightness(src1, 5, 0)
cv.waitKey(0)  # 等待一个按键输入后退出
cv.destroyAllWindows()  # 关闭所有窗口

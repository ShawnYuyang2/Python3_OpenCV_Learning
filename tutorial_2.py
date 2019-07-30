""""""""""
code:zx
time:2019.7.28
学习opencv读取、修改和创建图像
"""""""""""
import cv2 as cv
import numpy as np


def access_pixels(image):
    print(image.shape)
    height = image.shape[0]  # 高
    width = image.shape[1]   # 宽
    channels = image.shape[2]  # 通道
    print("width: %s ,height: %s, channels: %s" % (width, height, channels))
# 循环获取每一个像素点
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]  # pv是一个三维数组，存储了图片三个通道的所有像素点
                image[row, col, c] = 255 - pv  # 反色
    cv.imshow("pixels_demo", image)


# 利用np创建新的图像
def create_image():
    """"""""""
    img = np.zeros([400, 400, 3], np.uint8)  # 大小400X400，类型unsigned int 8位
    img[100:200, 100:200, 2] = np.ones([100, 100]) * 255  # 0通道赋值为255，蓝色
    cv.imshow("new image", img)
    

    img = np.ones([400, 400, 1], np.uint8)  # 单通道
    img = img * 255  # 127灰度白黑之间
    cv.imshow("new image", img)
    cv.imwrite("C:/Users/zx/Desktop/output.jpg", img)
    """""""""
    m1 = np.ones([3, 3], np.int8)
    m1 = cv.convertScaleAbs(m1)
    m1.fill(12222.388)
    print(m1)
    m2 = m1.reshape([1, 9])
    print(m2)
# blue,green,red三色通道组合起来才有彩色图像


src = cv.imread('C:/Users/zx/Desktop/test.jpg')   # 读图片,就是个数组了
# cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)  # 通过open_cv的GUI显示图像
cv.imwrite("C:/Users/zx/Desktop/result.jpg", src)
# 计时开始
t1 = cv.getTickCount()  # 获取当前cpu的时钟点数t1
# access_pixels(src)
create_image()
t2 = cv.getTickCount()  # 获取当前cpu的时钟点数t2
# 计时结束

cv.waitKey(0)  # 等待一个按键输入后退出
t = ((t2 - t1)/cv.getTickFrequency())
print("Spend Time: %s s" % t)  # cv.getTickFrequency()获取时钟频率
# 结果计算出来是毫秒为单位，换算成秒要乘1000
cv.destroyAllWindows()  # 关闭所有窗口

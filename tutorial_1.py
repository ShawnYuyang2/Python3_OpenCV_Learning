import cv2 as cv
import numpy as np

# #图像就是一个（或几个）矩阵组成的，图像有其属性：通道数目，高与宽，图像类型等

# ##读取图像的属性


def get_image_info(image):
    print(type(image))
    print('图像形状', image.shape)
    print('图像大小', image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)

# 读取视频


def video_demo():
    capture = cv.VideoCapture(0)  # 调用摄像头 0代表摄像头序号，或者也可以用视频文件路径
    while(1):
        ret, frame = capture.read()  # 读取摄像头 return frame(帧）
        frame = cv.flip(frame, 1)   # 图像镜像（flip）
        cv.imshow("video", frame)
        c = cv.waitKey(50)  # 50毫秒
        if c == 27:
            break


# #####读取图片并显示######

# src = cv.imread('C:/Users/zx/Desktop/test.jpg')   # 读图片,就是个数组了
# cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)  # 通过open_cv的GUI显示图像
# get_image_info(src)
video_demo()
cv.imwrite("C:/Users/zx/Desktop/result.jpg", src)
cv.waitKey(0)  # 等待一个按键输入后退出
cv.destroyAllWindows()  # 关闭所有窗口




import cv2 as cv

#读取图片并显示
src = cv.imread('C:/Users/zx/Desktop/jpg1.jpg')#读图片
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)#通过opcv的GUI显示图像
cv.waitKey(0)#等待一个按键输入后退出
cv.destroyAllWindows()#关闭所有窗口



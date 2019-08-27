import cv2
import os
import time
output_dir = r'C:/Users/zx/Desktop/photo'
cap = cv2.VideoCapture(0)
i = 1
while 1:
    ret, frame = cap.read()
    cv2.imshow('cap', frame)
    flag = cv2.waitKey(1)
    output_path = os.path.join(output_dir,  "%04d.jpg" % i)
    print("successful save photo %04d.jpg" % i)
    frame = cv2.resize(frame, None,
                       fx=0.5,
                       fy=0.5,
                       interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(output_path, frame)
    time.sleep(0.5)
    i += 1
    if flag == 27:  # 按下ESC键
        break


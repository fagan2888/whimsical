#coding:utf-8
import cv2
import numpy as np
import time,datetime
import sys

# if str(raw_input('over writer the output file?(y/n)'))=='y':
#     pass
# else:
#     sys.exit(-1)





camera = cv2.VideoCapture(0) # 参数0表示第一个摄像头

# 判断视频是否打开
if (camera.isOpened()):
    print('Open')
else:
    print('摄像头未打开')

# 设置camera的宽度和高度
# camera.set(cv2.CAP_PROP_FRAME_WIDTH,1920)
# camera.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)

# 测试用,查看视频size
width=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width,height)
print('size:'+repr(size))

def add_timestr(img):

    time_str= (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

    color=(255,255,255)
    if np.mean( img[height-20:height,0:300])>128:
        color=(0,0,0)
    cv2.putText(img, time_str, (0, height-10) ,cv2.FONT_HERSHEY_SIMPLEX ,0.8, color ,2)
    return img

es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 4))
kernel = np.ones((5, 5), np.uint8)
background = None
video_writer = cv2.VideoWriter('./CCTV/move_'+datetime.datetime.now().strftime("%m_%d_%H_%M")+'.flv', cv2.VideoWriter_fourcc('F','L','V','1'), 30, (width, height))
tend=0
while True:
    # 读取视频流
    grabbed, frame_lwpCV = camera.read()
    # 对帧进行预处理，先转灰度图，再进行高斯滤波。
    # 用高斯滤波进行模糊处理，进行处理的原因：每个输入的视频都会因自然震动、光照变化或者摄像头本身等原因而产生噪声。对噪声进行平滑是为了避免在运动和跟踪时将其检测出来。
    gray_lwpCV = cv2.cvtColor(frame_lwpCV, cv2.COLOR_BGR2GRAY)
    gray_lwpCV = cv2.GaussianBlur(gray_lwpCV, (21, 21), 0)

    # 将第一帧设置为整个输入的背景
    # if background is None:
    #     background = gray_lwpCV
    #     continue
    if background is None:
        background=gray_lwpCV
    else:

        background = frameold
    frameold=gray_lwpCV
    # 对于每个从背景之后读取的帧都会计算其与北京之间的差异，并得到一个差分图（different map）。
    # 还需要应用阈值来得到一幅黑白图像，并通过下面代码来膨胀（dilate）图像，从而对孔（hole）和缺陷（imperfection）进行归一化处理
    diff = cv2.absdiff(background, gray_lwpCV)
    diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1] # 二值化阈值处理
    diff = cv2.dilate(diff, es, iterations=2) # 形态学膨胀



    # cv2.imshow('diff',diff)
    # cv2.waitKey(1000)



    # 显示矩形框
    contours, hierarchy = cv2.findContours(diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # 该函数计算一幅图像中目标的轮廓
    add_timestr(frame_lwpCV)
    flag=0
    for c in contours:
        # if cv2.contourArea(c) < 1500: # 对于矩形区域，只显示大于给定阈值的轮廓，所以一些微小的变化不会显示。对于光照不变和噪声低的摄像头可不设定轮廓最小尺寸的阈值
        #     continue
        (x, y, w, h) = cv2.boundingRect(c) # 该函数计算矩形的边界框
        cv2.rectangle(frame_lwpCV, (x, y), (x+w, y+h), (0, 255, 0), 2)
        flag=1
    if flag==1:
        video_writer.write(frame_lwpCV)
        tend=time.time()
        print('Move detected at '+datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"))
        flag=0
    if time.time()-tend<3:
        video_writer.write(frame_lwpCV)
    else:
        pass
    cv2.imshow('contours', frame_lwpCV)
    cv2.imshow('dis', diff)

    key = cv2.waitKey(int(1000/30)) & 0xFF
    # 按'q'健退出循环
    if key == ord('q'):
        break
# When everything done, release the capture
camera.release()
cv2.destroyAllWindows()
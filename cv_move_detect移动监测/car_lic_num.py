# coding:utf-8

import cv2




import imutils

import sys
import os
import time
import pytesseract

def find_car_lic(image):
    resized = imutils.resize(image, width=300)
    ratio = image.shape[0] / float(resized.shape[0])  # 缩小倍数

    b, g, r = cv2.split(resized)

    # blurred = cv2.GaussianBlur(r, (5, 5), 0)
    thresh = cv2.threshold(r, 140, 255, cv2.THRESH_BINARY)[1]  # 85/212

    es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 4))  # 腐蚀内核
    # thresh = cv2.threshold(r, 25, 255, cv2.THRESH_BINARY)[1]  # 二值化阈值处理
    thresh = cv2.dilate(thresh, es, iterations=1)  # 形态学膨胀
    # canny=cv2.Canny(thresh,100,200)
    # cv2.imshow('canny',canny)

    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)  # 该函数计算一幅图像中目标的轮廓
    list = []
    for i, c in enumerate(contours):
        # if cv2.contourArea(c) < 1500: # 对于矩形区域，只显示大于给定阈值的轮廓，所以一些微小的变化不会显示。对于光照不变和噪声低的摄像头可不设定轮廓最小尺寸的阈值
        #     continue
        (x, y, w, h) = cv2.boundingRect(c)  # 该函数计算矩形的边界框

        w_h = float(w) / float(h)
        # if True:
        # 选择长宽比满足要求的
        if w_h > 2.5 and w_h < 3.5 and h > 15:
            cv2.rectangle(resized, (x, y), (x + w, y + h), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(resized, str(i), (x, y), font, 1.0, (255, 255, 255), 1)
            print(w, h, float(w) / float(h))
            break

    car = image[int(y * ratio):int((y + h) * ratio), int(x * ratio):int((x + w) * ratio)]
    cv2.imshow('car_lic', car)
    print(car.shape)
    cv2.waitKey(1000)
    cv2.destroyWindow('car_lic')
    return car


image=cv2.imread('.\car\car_lic.jpg')

# 得到车牌图片
car=find_car_lic(image)
b, g, r = cv2.split(car)
red=r

thresh=cv2.threshold(red,130,255,cv2.THRESH_BINARY)[1]
car_num=cv2.bitwise_not(thresh)
cv2.imwrite('imgs/car_num.jpg', car_num)
code=pytesseract.image_to_string(thresh)
print('car_plate=',code)

cv2.imshow('dila',car_num)
cv2.waitKey(10000)
cv2.destroyAllWindows()
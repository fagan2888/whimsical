import cv2
import imutils
image=cv2.imread('.\car\car2.jpg')
resized=imutils.resize(image,width=300)
#cv2.imshow('resize',resized)
gray=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
thresh0=cv2.threshold(gray,120,255,cv2.THRESH_BINARY)[1]
#cv2.imshow('th0',thresh0)


gray=cv2.GaussianBlur(gray,(3,3),0)

thresh1=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,5,7)
non_noise=cv2.fastNlMeansDenoising(thresh1,h=50)


es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (6, 2))
cv2.imshow('non_noise',non_noise)
# 这句不知道为什么出问题了
diff = cv2.dilate(non_noise, es, iterations=2)  # 形态学膨胀
#diff=non_noise
diff=cv2.threshold(diff,100,255,cv2.THRESH_BINARY)[1] # 对降噪后的图再次二值化

contours, hierarchy = cv2.findContours(diff.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)  # 该函数计算一幅图像中目标的轮廓
for c in contours:
    # if cv2.contourArea(c) < 1500: # 对于矩形区域，只显示大于给定阈值的轮廓，所以一些微小的变化不会显示。对于光照不变和噪声低的摄像头可不设定轮廓最小尺寸的阈值
    #     continue
    (x, y, w, h) = cv2.boundingRect(c)  # 该函数计算矩形的边界框
    #if w>10 and float(w)/float(h)>2.5 and float(w)/float(h)<3.2 :
    if True:
        cv2.rectangle(resized, (x, y), (x + w, y + h), (0, 255, 0), 2)
        flag = 1

cv2.imshow('thresh',thresh1)
cv2.imshow('diff',diff)
cv2.imshow('rect',resized)
cv2.waitKey(10000)
contour=cv2.findContours(non_noise,cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)[0]

for c in contour:
    cv2.drawContours(resized, [c], -1, (0, 255, 0), 2)

#cv2.imshow('th1',thresh1)
#cv2.imshow('non_noise',non_noise)
#cv2.imshow('resized2',resized)
cv2.waitKey(10000)
cv2.destroyAllWindows()
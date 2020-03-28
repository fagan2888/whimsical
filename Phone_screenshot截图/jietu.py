#coding:utf-8
# -*- encoding=utf8 -*-
__author__ = "puremilk"

from airtest.core.api import *

auto_setup(__file__)# -*- encoding=utf8 -*-
__author__ = "puremilk"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

import time,datetime

# 截图
def capture_mijia():
    keyevent("HOME")
    # 点击进入应用
    poco(text="米家").click()
    
    print(datetime.datetime.now())
    # 进入应用可能有卡顿，等待15s
    sleep(15)
    # 退出摄像头      
    # touch((80,180))
    #向上滑动确保在屏幕最下方
    swipe((500,1600), (500,300))

    #输出文件名字
    camera_name=[['反应器-二楼','三楼反应器','ATF-二楼'],['AKTA Awant25','一楼层析柜','AKTA Pilot']]
    
    # 几个摄像头的屏幕位置
    x_pos=[300,900]
    y_pos=[900,1200,1500]
    # 依次点击各个摄像头
    for i in range(2):
        for j in range(3):

            touch((x_pos[i],y_pos[j]))
            # 进入摄像头后等待加载(实际使用可以更长些）
            sleep(10)
            # 点击放大
            touch((1000,1000))
            # 等待大画面加载
            sleep(5)
            
            # 输出截图文件
            print(snapshot(filename='/Users/puremilk/Documents/airtest/test.air/截图文件/'+str(datetime.datetime.now().__format__('%m-%d %H-%M '))+camera_name[i][j]+'.jpg',msg="camera"))
            
            # 使用手机自带截图
            keyevent('SYSRQ')
            sleep(2)
            
            #退出全屏幕
            keyevent("BACK")
            sleep(1)
            # 退出摄像头      
            touch((80,180))
            #等待加载（其实可以不要）      
            sleep(1)
    return 0            
           

                
now_time=datetime.datetime.now().time()
need_time_list=[]
for i in range(11,12):
    need_time_list.append(datetime.time(i,24,0,0))
for i in range(6):
    need_time=need_time_list[0]
    while True:
        now_time=datetime.datetime.now().time()
        if need_time.__le__(now_time):
            print("now_time:    "+str(now_time.__format__('%H:%M:%S'))+'     next snap time: '+str(need_time.__format__('%H:%M:%S'))+'     snap now!!')

            capture_mijia()
            break
        else:
            print("now_time:    "+str(now_time.__format__('%H:%M:%S'))+'     next snap time: '+str(need_time.__format__('%H:%M:%S'))+'     keep waiting!')

            time.sleep(30)
    del need_time_list[0]
    
                  
                  
                  
                 
            







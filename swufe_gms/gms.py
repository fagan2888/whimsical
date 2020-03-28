#coding:utf-8
# 适用于SWUFE的研究生管理系统
# 加入学号和密码，修改课程ID
# 目前是对一个课程ID下的所有课程进行抢课
from selenium import webdriver
import time
import traceback
import re,sys,os


# from selenium.webdriver.chrome.options import Options
# chrome_options=Options()
# #设置chrome浏览器无界面模式
# chrome_options.add_argument('--headless')
# driver=webdriver.Chrome(chrome_options=chrome_options)
#
driver=webdriver.PhantomJS()

try:
    # 登陆界面
    login_url = 'https://gms.swufe.edu.cn'
    driver.get(login_url)
    driver.find_element_by_class_name('user').send_keys('你的学号')
    driver.find_element_by_class_name('psw').send_keys('你的密码')

    time.sleep(1)
    driver.find_element_by_class_name('subm').click()
    time.sleep(2)
except:
    print('cannot login!!!!!!!')
    sys.exit(1)

kcId_list=["4DAD83E23E1E1A06E0530B0AA8C0C238", # 房地产
           "E5F2E6F6601F15367328BDF86D2F5509", # 金融稳定
           "7299D2DC5C5F280A46B9656292A5C9F2"] # 财商论
           #"4DAD83E23E1A1A06E0530B0AA8C0C238"] # 货币政策理论

os.system('cls')
print('\r抢课课程门数==>',len(kcId_list))
print('正在抢课课程:')
for kc in kcId_list:
    print(kc)

count=0
while True:
    count+=1
    for kcId in kcId_list:
        try:

            # # 课程界面
            # lesson_url='http://gms.swufe.edu.cn/py/page/student/grkcgl.htm'
            # driver.get(lesson_url)
            # time.sleep(1)
            #
            # # 选择课程的退补选按钮
            # driver.find_element_by_id(kcId).click()

            # 选课按钮
            driver.get('http://gms.swufe.edu.cn/py/page/student/xkbjxxWindow.htm?kcId='+kcId)
            # 课程名称
            try:
                kc_name=re.findall('(?<=<td>).*?(?=</td>)',driver.page_source)[0].strip()
            except:
                print('get class name error')
                kc_name='NULL'
            # 获得课程容量
            class_all=re.findall('\d+/\d+/\d+',str(driver.page_source))
            # 同一个课程id下的不同课程
            for index,class_info in enumerate(class_all):
                class_num=class_info.split('/')
                print('\r','第',count,'轮尝试 ',kc_name,'　'*(15-len(kc_name)),index,class_num,sep='',end='',flush=True)

                # 获得课程人数
                now_num=int(class_num[0])
                max_num=int(class_num[2])

                if now_num<max_num:
                    # 点击对应的选课按钮
                    text=driver.find_elements_by_name(kcId)[index]
                    text.click()
                    time.sleep(1)
                    kcId_list.remove(kcId)
                    os.system('cls')
                    print('抢到课程===================',kc_name, ' ' * (15 - len(kc_name)), index, class_num)
                    print('Now num of class=', len(kcId_list))
                    print('目前抢课课程:')
                    for kc in kcId_list:
                        print(kc)
                    pass
                else:
                    pass


            # # 获取对话框
            # dig_alert = driver.switch_to.alert
            # time.sleep(1)
            # # 打印对话框内容
            # print(dig_alert.text)
            # choose=input('y/n?')
            # if choose=='y':
            #     dig_alert.accept()
            # else:
            #     dig_alert.dismiss()
            # # open('out.html','w').write(str(driver.page_source))


        except:
            traceback.print_exc()
            print('error!')
            pass


input('>>>press any key to quit')


driver.quit()
#coding:utf-8
# 修改课程id，运行这个文件
from selenium import webdriver
import time
import traceback
import re,sys,os

driver=webdriver.PhantomJS('./phantomjs.exe')
# driver=webdriver.Chrome()
user=str(input('学号：'))
psw=str(input('密码：'))
kcId=str(input('课程ID：'))
try:
    # 登陆界面
    login_url = 'https://gms.swufe.edu.cn'
    driver.get(login_url)
    driver.find_element_by_class_name('user').send_keys(user)
    driver.find_element_by_class_name('psw').send_keys(psw)
    time.sleep(0.1)
    driver.find_element_by_class_name('subm').click()
    time.sleep(1)

except:
    print('登录错误！')
    sys.exit(1)

if re.search('loginFailed',driver.page_source)!=None:
    print('系统错误！')
    sys.exit(1)

kcId_list=[kcId]
os.system('cls')
# print('\r抢课课程门数==>',len(kcId_list))
print('\r正在抢课课程:')
for kc in kcId_list:
    print(kc)

count=0

while True:
    for kcId in kcId_list:
        try:
            count+=1
            # 选课按钮
            driver.get('http://gms.swufe.edu.cn/py/page/student/xkbjxxWindow.htm?kcId='+kcId)
            # 课程名称
            try:
                kc_name=re.findall('(?<=<td>).*?(?=</td>)',driver.page_source)[0].strip()
            except:
                print('获取课程名称失败')
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
                    os.system('cls')
                    print('抢到课程===================',kc_name, ' ' * (15 - len(kc_name)), index, class_num)
                    # print('Now num of class=', len(kcId_list))
                    # print('目前抢课课程:')
                    driver.quit()
                    input('按任意键退出')
                    sys.exit(0)
                else:
                    pass


        except:
            traceback.print_exc()
            print('出现错误!')
            pass


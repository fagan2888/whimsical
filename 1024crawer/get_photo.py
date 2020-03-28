#coding:utf-8
import re,sys,threading,time,random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import os

# lock=threading.Lock()

file = open("all1.xml", 'r', encoding='utf-8')
content = file.read()
soup = BeautifulSoup(content,'lxml')
items = soup.find_all('article')
def get_img(html):
    img_list=[]
    soup=BeautifulSoup(html,'lxml')
    main_content=soup.find(name='div', attrs={"style": "border-top:0"}).find(name='div', attrs={"class": "tpc_content do_not_catch"})
    img_infos=main_content.find_all("input")
    if img_infos==[]:
        img_infos=main_content.find_all("img")
    for img_info in img_infos:
        img_url=img_info.get('data-src')
        img_list.append(img_url)
    return img_list


def request(url,num_retry=3):  ##这个函数获取网页的response 然后返回
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    UA = random.choice(user_agent_list) ##从self.user_agent_list中随机取出一个字符串（聪明的小哥儿一定发现了这是完整的User-Agent中：后面的一半段）
    headers = {'User-Agent': UA}  ##构造成一个完整的User-Agent （UA代表的是上面随机取出来的字
    try:
        content = requests.get(url, headers=headers,timeout=(5, 120))
        return content
    except:
        if num_retry>0:
            time.sleep(0.5)
            print(url+' try again')
            request(url,num_retry-1)
        else:
            return -1


def save(path,name,img_url):  ##这个函数保存图片
    path = path.strip()
    try:
        # lock.acquire()
        # try:
        #     img = request(img_url)
        # finally:
        #     lock.release()
        img=request(img_url)
    except:
        print(img_url+' cannot download photo')
        return -1
    if img!=-1 and img!=None:
        f = open('1024\\'+path+'\\'+str(name) + '.jpg', 'ab')
        f.write(img.content)
        f.close()
        print(img_url+' get')
    else:
        print(img_url+' 3 times download error')


def mkdir( path):  ##这个函数创建文件夹
    path = path.strip()
    isExists = os.path.exists(os.path.join("1024", path))
    if not isExists:
        print(u'建了一个名字叫做', path, u'的文件夹！')
        os.makedirs(os.path.join("1024", path))
        #os.chdir(os.path.join("1024", path))  ##切换到目录
        return True
    else:
        print(u'名字叫做', path, u'的文件夹已经存在了！')
        return False

for item in items:
    url=item.url
    title=str(item.get('title'))
    #print(title)
    print(url.text)#.replace('t66y.com','cb.wpio.xyz'))

    res=requests.get(url.text)#.replace('t66y.com','cb.wpio.xyz'))
    html=res.text.encode('utf-8')
    #print(html)
    try:
        img_list=get_img(html)
    except:
        print('get img list error')
        continue
    mkdir(title)
    tlist=[]
    for index,img in enumerate (img_list):
        try:
            if re.search('http.*?\.(jpg|png|gif|jpeg|JPG)', img) != None:
                t = threading.Thread(target=save, args=(title, index, img))
                tlist.append(t)
                t.start()
        except:
            print('some error')
    for i in range(len(tlist)):
        tlist[i].join()
    print('this page all finished')





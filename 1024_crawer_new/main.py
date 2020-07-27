#coding:utf-8
import requests
import threading

import re,os,time
from bs4 import BeautifulSoup

page_headers={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'Connection': 'keep-alive',
'Host': '11zipai.club',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.44'

}

img_headers={
'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'referer': 'https://11zipai.club/selfies/201906/85519.html',
'sec-fetch-dest': 'image',
'sec-fetch-mode': 'no-cors',
'sec-fetch-site': 'cross-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.44'
}




def get_page_html():
    page_list=[]
    for i in range(3):
        url='https://11zipai.club/e/space/ulist.php?page={}&mid=1&line=25&tempid=10&orderby=&myorder=0&userid=7744&totalnum=58'.format(i)

        res=requests.get(url)
        text=res.text
        print(text)
        this_page=re.findall('(?<=href=")/.*?html',text)
        page_list+=this_page

    with open('page_list.txt','w') as f:
        f.write('\n'.join(page_list))
        f.close()


def fetch_img(img_url,ind,index,full_url):
    print(img_url)
    img_headers['referer']=full_url
    try:
        r=requests.get(img_url,headers=img_headers,timeout=60)
    except Exception as e:
        print('错误类型是', e.__class__.__name__)
        print('错误明细是', e)

        # r.close() # 出错了就没有r了，不用close 
        return 1


    if r.status_code ==200:
        with open('./img/{}/{}.jpg'.format(ind,index),'wb') as f:
            f.write(r.content)
            f.close()

    else:
        print(img_url,'cannot download')
    print('.',end='')
    r.close()


def img_html():
    with open('page_list.txt','r') as f:
        urls=f.readlines()
    for ind,url in enumerate(urls):
        if ind<19:
            continue
        full_url=('https://11zipai.club'+url).strip()
        print(full_url)
        res=requests.get(full_url,headers=page_headers)
        # print(res.text.encode('utf-8'))
        # title=re.findall('(?<=<title>).*?(?=</title>)',res.text)[0]
        # print(title) # error encode
        if str(ind) not in os.listdir('./img/'):
            os.mkdir('./img/'+str(ind))
        img_list=re.findall('https://pic.zipai.buzz.*?.jpg',res.text)
        thread_list=[]
        for index,img_url in enumerate(img_list):
            t=threading.Thread(target=fetch_img,args=(img_url,ind,index,full_url),name=str(index))
            thread_list.append(t)

        for j in range(len(img_list)):
            thread_list[j].start()
            while threading.active_count() > 20:
                time.sleep(1)
        # for j in range(len(img_list)):
        thread_list[len(img_list)-1].join()
        res.close()


def page_name(): # 获取每个的名字，之前编码有点问题所以没有获取到
    title_list=[]
    for i in range(3):
        url = 'https://11zipai.club/e/space/ulist.php?page={}&mid=1&line=25&tempid=10&orderby=&myorder=0&userid=7744&totalnum=58'.format(i)

        res = requests.get(url)
        text = res.text
        text=text.encode('utf-8')
        text=text.decode('utf-8')
        soup=BeautifulSoup(text,'lxml')
        content=soup.find_all('div',class_='user-right')[0]
        rows=content.find_all('li')
        for row in rows:
            title=row.find_all('a')[0]
            title_list.append(title.text)
    print('\n'.join(title_list))

    with open('name.txt','w',encoding='utf-8') as f:
        f.write('\n'.join(title_list))
        f.close()


def update_file_name():
    file_path='./img/'
    with open('name.txt', 'r', encoding='utf-8') as f:
        name_list=f.readlines()
        f.close()
    for i in range(58):
        if str(i) in os.listdir(file_path):
            os.rename(file_path+str(i),file_path+str(i).zfill(2)+'_'+name_list[i].strip())



# img_html()


# page_name()

update_file_name()
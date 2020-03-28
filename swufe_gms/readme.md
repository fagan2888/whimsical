# SWUFE 的研究生系统抢课

1. 适用于SWUFE的研究生管理系统
2. 课程ID可以在课程详情页的网址中看到，例如
    > http://gms.swufe.edu.cn/py/page/student/xkkcxx.htm?kcId=4DAD83E23E1E1A06E0530B0AA8C0C238
    的课程id为4DAD83E23E1E1A06E0530B0AA8C0C238
3. 加入学号和密码，修改课程ID
4. 目前是对一个课程ID下的所有课程进行抢课
5. 其实好像目前对于程序的结束的判定还有点问题，理论上会一直试图抢课（gms_release.exe文件不会）

主要程序是gms.py

打包了一个gms_release.exe文件方便运行

目前exe文件只能对单个课程ID进行抢课

需要输入学号，密码和课程ID，且需要**phantomjs.exe文件和gms_release.exe在同目录下**

>Email：zikepeng@outlook.com
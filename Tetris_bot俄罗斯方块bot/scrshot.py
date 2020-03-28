from PIL import ImageGrab,Image
import time

##################
##################
I_array=[['.', '.', '.', '.'], ['.', '.', '.', '.'], ['0', '0', '0', '0'], ['.', '.', '.', '.']]
J_array=[['.', '.', '.', '.'], ['0', '.', '.', '.'], ['0', '0', '0', '0'], ['.', '.', '.', '.']]
L_array=[['.', '.', '.', '.'], ['.', '.', '.', '0'], ['0', '0', '0', '0'], ['.', '.', '.', '.']]
O_array=[['.', '.', '.', '.'], ['.', '0', '0', '.'], ['.', '0', '0', '.'], ['.', '.', '.', '.']]
S_array=[['.', '.', '.', '.'], ['.', '0', '0', '0'], ['0', '0', '0', '.'], ['.', '.', '.', '.']]
T_array=[['.', '.', '.', '.'], ['.', '0', '0', '.'], ['0', '0', '0', '0'], ['.', '.', '.', '.']]
Z_array=[['.', '.', '.', '.'], ['0', '0', '0', '.'], ['.', '0', '0', '0'], ['.', '.', '.', '.']]
I2_array=[['.', '.', '.', '.'], ['0', '0', '0', '0'], ['0', '0', '0', '0'], ['.', '.', '.', '.']]
tot_word=['I','J','L','O','S','T','Z','I','---------error']
tot_array=[I_array,J_array,L_array,O_array,S_array,T_array,Z_array,I2_array]
##################
def get_photo(small_img,num):
    # small_img.show()
    if num==0:
        tot=60
    if num==1:
        tot=50
    if num==2:
        tot=40
    if mode ==1 :
        tot=50
    d=4
    unit = int(tot / d)
    u0 = int(unit / 2)
    pixel2 = [[0] * d for i in range(d)]
    for i in range(0, d):
        for j in range(0, d):
            small_pix = (small_img.getpixel((u0 + unit * i, u0 + unit * j)))
            if small_pix < 50:
                pixel2[j][i] = '.'
            else:
                pixel2[j][i] = '0'
    output=1
    if output:
        for p in pixel2:
            for i in p:
                print i,
            print ' '
    return pixel2
def get_screenshot(num):
    im = ImageGrab.grab()
    #print 'info:',format(im.size)
    #im.save('1.jpg','jpeg')
    #print 'save~'
    # #im.show()
    if num==0:
        #x=307
        #y=171
        x=867
        y=413
        tot=60
    if num==1:
        x = 312+560
        y = 241+242
        tot=50
    if num==2:
        x =317+560
        y =301+242
        tot=40
    if mode == 1:
        x=x+35
        y=y+5
        tot=50
    print x,y,tot
    small_img=im.crop((x,y,x+tot,y+tot)).convert('L')
    small_img.show()
    small_img.save('./wtf/'+str(num)+'_bianda.bmp','bmp')
    #raw_input()

    pixel=get_photo(small_img,num)
    flag=0
    for i in range(0,8):
        if pixel==tot_array[i]:
            #print '>>'*(3-num),tot_word[i]
            flag=1
            return i
        else:
            #print 'not',tot[i]
            pass
    if flag==0:
        #print '---------------------error'
        return 8

global mode
mode =1

next=[8]*6
while 1:

    for num in range(0,1):
        next[num]=get_screenshot(num)
    flag=0
    for i in range (0,3):
        if next[i]==next[i+3]:##if not change
            pass
        else:#if change
            flag=1

            next[i+3]=next[i]
            if i ==1:
                if next[i]!=next[i+4]:
                    print 'something passed!!!!'
    if flag:
        for i in range (0,3):
            print '>>' * (3 - i), tot_word[next[i]]

    break
    time.sleep(0.5)



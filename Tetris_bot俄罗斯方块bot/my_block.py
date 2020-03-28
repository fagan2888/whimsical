     #coding:utf-8
from PIL import ImageGrab,Image
import time
from pynput.keyboard import Key, Controller

##################
##################
I_array=[['.', '.', '.', '.'], ['.', '.', '.', '.'], ['0', '0', '0', '0' ], ['.', '.', '.', '.']]
J_array=[['.', '.', '.', '.'], ['0', '.', '.', '.'], ['0', '0', '0', '0'], ['.', '.', '.', '.']]
L_array=[['.', '.', '.', '.'], ['.', '.', '.', '0'], ['0', '0', '0', '0'], ['.', '.', '.', '.']]
O_array=[['.', '.', '.', '.'], ['.', '0', '0', '.'], ['.', '0', '0', '.'] , ['.', '.', '.', '.']]
S_array=[['.', '.', '.', '.'], ['.', '0', '0', '0'], ['0', '0', '0', '.'], ['.', '.', '.', '.']]
T_array=[['.', '.', '.', '.'], ['.', '0', '0', '.'], ['0', '0', '0', '0'], ['.', '.', '.', '.']]
Z_array=[['.', '.', '.', '.'], ['0', '0', '0', '.'], ['.', '0', '0', '0'],  ['.', '.', '.', '.']]
I2_array=[['.', '.', '.', '.'], ['0', '0', '0', '0'], ['0', '0', '0', '0'], ['.', '.', '.', '.']]
tot_word=['I','J','L','O','S','T','Z','I','error']
tot_array=[I_array,J_array,L_array,O_array,S_array,T_array,Z_array,I2_array ]


z_type_0=[['*','*','.'],['.','*','*']]
z_type_1=[['.','*'],['*','*'],['*','.' ]]
z_type_all=[z_type_0,z_type_1]
o_type_all=[[['*','*'],['*','*']]]
i_type_all=[[['*','*','*','*']],[['*'],['*'],['*'],['*']]]
s_type_all=[[['.','*','*'],['*','*','.']],[['*','.'],['*','*'],['.','*']]]
l_type_0=[['.','.','*'],['*','*','*']]
l_type_1=[['*','.'],['*','.'],['*','*']]
l_type_2=[['*','*','*'],['*','.','.']]
l_type_3=[['*','*'],['.','*'],['.','*']]
l_type_all=[l_type_0,l_type_1,l_type_2,l_type_3]
j_type_0=[['*','.','.'],['*','*','*']]
j_type_1=[['*','*'],['*','.'],['*','.']]
j_type_2=[['*','*','*'],['.','.','*']]
j_type_3=[['.','*'],['.','*'],['*','*']]
j_type_all=[j_type_0,j_type_1,j_type_2,j_type_3]
t_type_0=[['.','*','.'],['*','*','*']]
t_type_1=[['*','.'],['*','*'],['*','.']]
t_type_2=[['*','*','*'],['.','*','.']]
t_type_3=[['.','*'],['*','*'],['.','*']]
t_type_all=[t_type_0,t_type_1,t_type_2,t_type_3]

type_all=[z_type_all,o_type_all,i_type_all,s_type_all,l_type_all,j_type_all,t_type_all]

##################
def get_photo(small_img,num):
    # small_img.show()
    if num==0:
        tot=60
    if num==1:
        tot=50
    if num==2:
        tot=40
    if mode ==1:
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
    output=0
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
        x=307+560
        y=171+242
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
        x+=35##实际位置只加了30，但是缩小了5
        y+=5
        tot-=10
    small_img=im.crop((x,y,x+tot,y+tot)).convert('L')
    # small_img.show()
    #small_img.save('./block/'+str(num)+'_I.bmp','bmp')
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

def get_black_pic():
    from PIL import ImageGrab
    im = ImageGrab.grab()
    #print 'info:', format(im.size)
    # im.save('1.jpg','jpeg')
    # print 'save~'
    # #im.show()
    x = 97+560
    y = 132+242
    if mode == 1:
        x=687# +30
        #y=373#
    h = 360
    w = 180
    unit = 18
    small_img = im.crop((x, y, x + w, y + h))
    #small_img.show()
    #small_img.save('black.bmp', 'bmp')
    # raw_input()
    return small_img

def get_black_status():
    img=get_black_pic()
    #img=Image.open('black.bmp')
    grey_img=img.convert('L')
    unit=18
    pixel=[['.']*10for i in range(20)]

    print '>>>'
    for width in range(0,10):
        for height in range(1 ,20):
            pix=(grey_img.getpixel((9+unit*width,9+unit*height)))
            #print pix
            if pix<128:   #50
                pixel[height][width]='.'
            else:
                pixel[height][width]='0'

    for i in range(19):
        for j in range(10):
            if pixel[i][j]=='0':
                if j!=0 and j!=9 :
                    if pixel[i-1][j]=='.' and pixel[i+1][j]=='.'and pixel[i][j+1]=='.'and pixel [i][j-1]=='.':
                        pixel[i][j]='.'
                    else:
                        pass
                elif j==0:
                    if pixel[i-1][j]=='.' and pixel[i+1][j]=='.'and pixel[i][j+1]=='.':
                        pixel[i][j]='.'
                    else:
                        pass
                elif j==9:
                    if pixel[i-1][j]=='.' and pixel[i+1][j]=='.'and pixel [i][j-1]=='.':
                        pixel[i][j]='.'
                    else:
                        pass

    #print pixel

    return pixel

def occupy(x,z_type,now_type):
    distance_list = []
    for i in range(len(z_type)):
        for j in range(len(z_type[0])):
            if z_type[i][j] == '*':
               #print '>>>', i, j
                for distance in range(20-i):
                    if now_type[i + distance][x+j] == '0':
                        #print 'occpy'
                        #print 'distance=',distance
                        distance_list.append(distance - 1)
                        break
                    elif i+distance>=19:
                        #print 'bottom'
                        #print 'distance=',distance
                        distance_list.append(distance)
            else:
                pass
                #print '<<<', i, j
    #print 'distance list=',distance_list,
    return min(distance_list)

def if_clear(now_type):
    row_clear=0
    star_num = 0
    row_num=0
    for row in now_type:
        flag=0
        star_num_buff=0
        for point in row:
            if point=='.':
                flag=1
                break
            if point=='*':
                star_num_buff+=1
        row_num+=1
        if flag==0:
            print 'row_num',row_num
            for i in range(1,row_num):
                now_type[row_num - i] = now_type[row_num - i - 1]
            now_type[0] = ['.'] * 10
            row_clear+=1
            star_num+=star_num_buff
            break
    modulus=0
    cou=[[1,-1 ],[2,1],[3,3],[4,9]]
    for i in range(4):
        if row_clear==cou[i][0]:
            modulus=cou[i][1]
            break
    return now_type,modulus*star_num

def get_Row_Trans(now_type):
    row_trans=0
    for row in now_type:
        pre_color=1
        for i in range(10):
            if row[i]=='.':
                now_color=0
            else:
                now_color=1
            if now_color==pre_color:
                pass
            else:
                row_trans+=1
                pre_color=now_color

    return row_trans

def get_colum_trans(now_type):
    colnum_trans = 0
    for colnum in range(10):
        pre_color=1
        for row in range(20):
            if now_type[row][colnum]=='.':
                now_color=0
            else:
                now_color=1
            if now_color==pre_color:
                pass
            else:
                colnum_trans+=1
                pre_color=now_color
    return colnum_trans

def empty_hole(now_type):
    empty_hole=0
    for colnum in range(10):
        flag=0
        for row in range(20):
            if flag==0:
                if now_type[row][colnum]=='.':
                    pass
                else:
                    flag=1
            else:
                if now_type[row][colnum] == '.':
                    empty_hole+=1

    return empty_hole

def well_num(now_type):
    well_num=0
    for row in now_type:
        row.insert(0,'0')
        row.append('0')
        for i in range(10):
            if row[i]=='.' and row[i+1]!='.' and row[i-1]!='.':
                well_num+=1
    return well_num

def control_keyboard(x,direction,shape):
    keyboard = Controller()
    for i in range(direction-1):
        print 'hit up'
        keyboard.press(Key.up)
        time.sleep(0.025)
        keyboard.release(Key.up)
        time.sleep(0.025)
    couple=[['Z',0],['O',1],['I',2],['S',3],['L',4],['J',5],['T',6]]

    if shape==1:
        x0=4
    elif shape==2 and direction==2:
        x0=5
    elif shape==6 and direction==2:
        x0=4
    elif shape==3 and direction==2:
        x0=4
    elif shape==4 and direction==2:
        x0=4
    elif shape==5 and direction==2:
        x0=4
    elif shape==0 and direction==2:
        x0=4
    else:
        x0=3
    print 'x0=:',x0
    if x - x0 > 0:
        for i in range(x - x0):
            print "hit right"
            keyboard.press(Key.right)
            time.sleep(0.025)
            keyboard.release(Key.right)
            time.sleep(0.025)
    else:
        for i in range(x0 - x):
            print 'hit left'
            keyboard.press(Key.left)
            time.sleep(0.025)
            keyboard.release(Key.left)
            time.sleep(0.025)

    print 'over'
    '''
    keyboard.press(Key.space)
    time.sleep(0.15)
    keyboard.press(Key.space)
    '''
    #time.sleep(1)

def get_catelog(shape):
    #time.sleep(0.5)
    print 'the shape is ',shape
    origin_type=get_black_status()
    now_type=[['.']*10 for i in range(20)]
    couple=[['Z',0],['O',1],['I',2],['S',3],['L',4],['J',5],['T',6]]
    for coup in couple:
        if shape==coup[0]:
            shape_num=coup[1]
            print 'shape num==',shape_num
            break
    rating_0=[-10000,-1,-1,0]#rating,direction,x-axis,distance
    #now_type=[[0]*10 for i in range(20)]
    direction=0
    for z_type in type_all[shape_num]:#不同方向
        direction+=1
        for x in range(10-len(z_type[0])+1):#不同的x轴取值
            #################################刷新nowtype
            for i in range(20):
                for j in range(10):
                    now_type[i][j]=origin_type[i][j]
             #p rint '----------',origin_type[12][0]
            #print now_type

            distance=occupy(x,z_type,now_type)
            for i in range(len(z_type)):
                for j in range(len(z_type[0])):
                    if z_type[i][j]!='.':
                        now_type[i+distance][j+x]=z_type[i][j]
            '''#output the result
            for i in range(20):
                for j in range(10):
                    print now_type[i][j],
                print ' '
            '''
            now_type,erodedPieceCellsMetric=if_clear(now_type)
            landingHeight=20-distance+len(z_type)
            boardRowTransitions=get_Row_Trans(now_type)
            boardColTransitions=get_colum_trans(now_type)
            boardBuriedHoles=empty_hole(now_type)
            boardWells=well_num(now_type)
            '''
            print 'landingHeight',landingHeight
            print 'erodedPieceCellsMetric',erodedPieceCellsMetric
            print  'boardRowTransitions',boardRowTransitions
            print 'boardColTransitions',boardColTransitions
            print 'boardBuriedHoles',boardBuriedHoles
            print 'boardWells',boardWells
            '''
            rating = (-4.5)*landingHeight+(4.4)*erodedPieceCellsMetric + (-3.2) * boardRowTransitions + (-9.3) * boardColTransitions+ (-7.8) * boardBuriedHoles+ (-3.3) * boardWells;
            #print rating
            if rating >rating_0[0]:
                rating_0[0]=rating
                rating_0[1]=direction#1:不按空格
                rating_0[2]=x
                rating_0[3]=distance-1
            #print rating



    print 'highest_rating',int(rating_0[0])
    print 'direction:', rating_0[1]
    print 'move to:', rating_0[2]
    print 'distance:', rating_0[3]
    #time.sleep(1)


    # print '----------',origin_type[12][0]
    # print now_type
    for i in range(20):
        for j in range(10):
            now_type[i][j] = origin_type[i][j] 
    distance =rating_0[3]
    direction=rating_0[1]
    x=rating_0[2]
    last_type=type_all[shape_num][direction-1]#the type we choose
    print 'len:'
    print len(last_type),len(last_type[0])
    print last_type
    for i in range(len(last_type)):
        for j in range(len(last_type[0])):
            if last_type[i][j] != '.':
                print 'i,j,distane,x',i,j,distance,x
                now_type[i + distance+1][j + rating_0[2]] = last_type[i][j]

    for i in range(20):
        for j in range(10):
            print now_type[i][j],
        print ' '

    control_keyboard(rating_0[2],rating_0[1],shape_num)
    get_next_block()

def get_next_block():
    next=[8]*6
    #while 1:
    '''
        for num in range(0,3):
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
    '''
    next[0]=get_screenshot(0)
    print next[0]
    while next[0]==8:
        '''
        print 'try to click mouse '
        from pynput.mouse import Button
        from pynput.mouse import Controller as mm
        mouse=mm()
        mouse.position=(780,700)
        mouse.click(Button.left)
        mouse.release(Button.left)
        time.sleep(3)
        print 'error,have the next try five second later'
        '''
        time.sleep(0.5)
        next[0]=get_screenshot(0)
    Controller() .press(Key.space)
    time.sleep(0.03)
    Controller(). release(Key.space)
    print '======================================'
    print 'hit spa ce,start to next move'
    time.sleep(0.2)##等待消除白条   0.5heshi
    #time.sleep(1.5)
    get_catelog(tot_word[next[0]])

global mode

mode=0

time.sleep(2)

origin_type=get_black_status()

get_next_block()
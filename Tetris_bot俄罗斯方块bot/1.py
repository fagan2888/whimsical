#coding:utf-8
#origin_type=[['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '0', '0', '.', '.', '.', '.'], ['.', '.', '.', '.', '0', '0', '0', '.', '.', '.'], ['.', '.', '.', '.', '.', '0', '0', '.', '.', '.'], ['.', '.', '.', '.', '.', '0', '0', '.', '0', '.'], ['.', '.', '.', '0', '.', '0', '0', '0', '0', '0'], ['.', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['.', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['.', '.', '0', '0', '0', '0', '0', '0', '0', '0'], ['.', '.', '0', '0', '0', '0', '0', '0', '0', '0'], ['.', '.', '0', '0', '0', '0', '0', '0', '0', '.'], ['.', '.', '.', '0', '0', '0', '0', '0', '0', '0']]
origin_type=[['.']*10 for i in range(20)]


def get_black_pic():
    from PIL import ImageGrab
    im = ImageGrab.grab()
    #print 'info:', format(im.size)
    # im.save('1.jpg','jpeg')
    # print 'save~'
    # #im.show()
    x = 96
    y = 132
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
        for height in range(3,20):
            pix=(grey_img.getpixel((9+unit*width,9+unit*height)))
            #print pix
            if pix<50:
                pixel[height][width]='.'
            else:
                pixel[height][width]='0'
    '''
    for p in pixel:
        for i in p:
            print i,
        print ' '
    #print pixel
    '''
    return pixel
origin_type=get_black_status()
for i in range(20):
    for j in range(10):
        print origin_type[i][j],
    print ' '

z_type_0=[['*','*','.'],['.','*','*']]
z_type_1=[['.','*'],['*','*'],['*','.']]
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

def occupy(x):
    distance_list = []
    for i in range(len(z_type)):
        for j in range(len(z_type[0])):
            if z_type[i][j] == '*':
                print '>>>', i, j
                for distance in range(20-i):
                    if now_type[i + distance][x+j] == '0':
                        print 'occpy'
                        print distance
                        distance_list.append(distance - 1)
                        break
                    elif i+distance>=19:
                        print 'bottom'
                        distance_list.append(distance)
            else:
                print '<<<', i, j
    print distance_list
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
    return now_type,row_clear*star_num

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

rating_0=[-10000,[],-1,-1]
now_type=[[0]*10 for i in range(20)]
direction=0
for z_type in type_all[4]:#不同方向
    direction+=1
    for x in range(10-len(z_type[0])+1):#不同的x轴取值
        for i in range(20):
            for j in range(10):
                now_type[i][j]=origin_type[i][j]
        #print '----------',origin_type[12][0]
        #print now_type
        distance=occupy(x)
        for i in range(len(z_type)):
            for j in range(len(z_type[0])):
                if z_type[i][j]!='.':
                    now_type[i+distance][j+x]=z_type[i][j]

        for i in range(20):
            for j in range(10):
                print now_type[i][j],
            print ' '
        now_type,erodedPieceCellsMetric=if_clear(now_type)
        landingHeight=20-distance+len(z_type)
        boardRowTransitions=get_Row_Trans(now_type)
        boardColTransitions=get_colum_trans(now_type)
        boardBuriedHoles=empty_hole(now_type)
        boardWells=well_num(now_type)
        rating = (-1.0)*landingHeight+( 1.0)*erodedPieceCellsMetric + (-1.0) * boardRowTransitions + (-1.0) * boardColTransitions+ (-4.0) * boardBuriedHoles+ (-1.0) * boardWells;
        if rating >rating_0[0]:
            rating_0[0]=rating
            rating_0[1]=z_type
            rating_0[2]=x
            rating_0[3]=direction
        print rating

print 'direction=',rating_0[3]
print 'highest_rating',rating_0
#coding:utf-8

from maze_env import Maze
#chessboard=[[1,0,0],[0,1,-1],[-1,0,1]]
chessboard=[[0,0,0],[0,0,0],[0,0,0]]

def if_win(chessboard):
    for i in range(0,3):

        #竖向三个
        if sum(chessboard[j][i] for j in range(0,3))==3:
            return 1
        elif sum(chessboard[j][i] for j in range(0, 3)) == -3:
            return -1

        # 横向三个
        if sum(chessboard[i][j] for j in range(0,3))==3:
            return 1
        elif sum(chessboard[i][j] for j in range(0, 3)) == -3:
            return -1
        else:
            pass

    # 斜向三个
    if sum(chessboard[i][i] for i in range(0,3))==3:
        return 1
    elif sum(chessboard[i][i] for i in range(0,3))==-3:
        return -1
    elif sum(chessboard[i][2-i] for i in range(0,3))==3:
        return 1
    elif sum(chessboard[i][2-i] for i in range(0,3))==-3:
        return -1
    else:
        return 0

# o用1表示，x用-1表示
def display_board(chessboard):
    for i in range(0,3):
        for j in range(0,3):
            if chessboard[i][j]==0:
                print(' ',end=' ')
            elif chessboard[i][j]==1:
                print('o',end=' ')
            elif chessboard[i][j]==-1:
                print('x',end=' ')
        print('\n',end='')

def choose(chessboard,person_flag,pos):
    if chessboard[pos[0]][pos[1]]!=0:
        print('Already have Pieces, choose another place.')
        return chessboard,1
    else:
        chessboard[pos[0]][pos[1]]=person_flag
        return chessboard,0


person_flag=1
def update():
    person_flag=1
    env.reset()
    click_pos=env.mouse_coords()
    if person_flag==1:
        env.creat_o(click_pos)
        person_flag=0-person_flag
        return click_pos

    if person_flag == -1:
        env.creat_x(click_pos)
        person_flag = 0 - person_flag
        return click_pos



env=Maze()
env.after(100, update)
env.mainloop()

while True:
    if person_flag==1:
        print("now is the 'o'")
    else:
        print("now is the 'x'")
    pos=input('input position: eg. 0,1 is row 0, col 1')
    pos=pos.split(',')
    pos[0]=int(pos[0])
    pos[1]=int(pos[1])
    chessboard, occupy_flag=choose(chessboard,person_flag,pos)
    # 如果落子位置已经有棋子，则重新选择
    if occupy_flag:
        continue
    display_board(chessboard)
    win_flag = if_win(chessboard)
    if win_flag == 1:
        print('==o win!')
        break
    elif win_flag == -1:
        print('==x win!')
        break
    else:
        person_flag=0-person_flag
        pass


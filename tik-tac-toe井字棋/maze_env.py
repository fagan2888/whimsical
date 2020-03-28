"""
Reinforcement learning maze example.

Red rectangle:          explorer.
Black rectangles:       hells       [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].

This script is the environment part of this example. The RL is in RL_brain.py.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

import numpy as np
import time
import sys
if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk

UNIT = 40   # pixels
MAZE_H = 3  # grid height
MAZE_W = 3  # grid width


class Maze(tk.Tk, object):
    def __init__(self):
        super(Maze, self).__init__()
        self.title('maze')
        self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_H * UNIT))
        self.person_flag=1
        self.chessboard=[[0,0,0],[0,0,0],[0,0,0]]
        self._build_maze()
        print("now is the 'o'")


    def choose(self,chessboard, person_flag, pos):
        if chessboard[pos[0]][pos[1]] != 0:
            print('Already have Pieces, choose another place.')
            return chessboard, 1
        else:
            chessboard[pos[0]][pos[1]] = person_flag
            if person_flag == 1:
                self.creat_o(pos)
            else:
                self.creat_x(pos)
            return chessboard, 0


    def if_win(self,chessboard):


        for i in range(0, 3):

            # 竖向三个
            if sum(chessboard[j][i] for j in range(0, 3)) == 3:
                for k in range(0,3):
                    self.creat_o([k,i],1)
                return 1

            elif sum(chessboard[j][i] for j in range(0, 3)) == -3:
                for k in range(0,3):
                    self.creat_x([k,i],1)
                return -1

            # 横向三个
            if sum(chessboard[i][j] for j in range(0, 3)) == 3:
                for k in range(0,3):
                    self.creat_o([i,k],1)
                return 1
            elif sum(chessboard[i][j] for j in range(0, 3)) == -3:
                for k in range(0,3):
                    self.creat_x([i,k],1)
                return -1
            else:
                pass

        # 斜向三个
        if sum(chessboard[i][i] for i in range(0, 3)) == 3:
            for k in range(0, 3):
                self.creat_o([k, k], 1)
            return 1
        elif sum(chessboard[i][i] for i in range(0, 3)) == -3:
            for k in range(0, 3):
                self.creat_x([k, k], 1)
            return -1
        elif sum(chessboard[i][2 - i] for i in range(0, 3)) == 3:
            for k in range(0, 3):
                self.creat_o([k, 2-k], 1)
            return 1
        elif sum(chessboard[i][2 - i] for i in range(0, 3)) == -3:
            for k in range(0, 3):
                self.creat_x([k, 2-k], 1)
            return -1

            # 平局
        elif sum(chessboard[i].count(0) for i in range(0, 3)) == 0:
            return -2


        else:
            return 0


    def process_result(self,chessboard):
        win_flag = self.if_win(chessboard)
        if win_flag == 1:
            print('==o win!')
            time.sleep(2)
            self.reset()
        elif win_flag == -1:
            print('==x win!')
            time.sleep(2)
            self.reset()
        elif win_flag == -2:
            print('==Draw')
            time.sleep(2)
            self.reset()
        else:
            self.person_flag = 0 - self.person_flag
            if self.person_flag == 1:
                print("now is the 'o'")
            if self.person_flag == -1:
                print("now is the 'x'")
            pass


    def mouse_coords(self,event):
        pos=[int(event.x/40), int(event.y/40)]
        print(pos)

        chessboard, occupy_flag = self.choose(self.chessboard, self.person_flag, pos)
        # 如果落子位置已经有棋子，则重新选择
        if occupy_flag:
            return 0
        self.process_result(chessboard)


    def _build_maze(self):
        self.canvas = tk.Canvas(self, bg='white',
                           height=MAZE_H * UNIT,
                           width=MAZE_W * UNIT)
        # create grids
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_W * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)
        self.canvas.bind("<Button 1>", self.mouse_coords)
        self.canvas.pack()


    def creat_o(self,pos,preview_flag=0):
        if preview_flag:
            color='red'
        else:
            color='black'
        origin = np.array([20, 20])
        o_center = origin + [UNIT*pos[0],UNIT*pos[1]]
        self.o_pieces = self.canvas.create_oval(
            o_center[0] - 15, o_center[1] - 15,
            o_center[0] + 15, o_center[1] + 15,
            fill=color)
        self.o_pieces = self.canvas.create_oval(
            o_center[0] - 10, o_center[1] - 10,
            o_center[0] + 10, o_center[1] + 10,
            fill='white')
        self.canvas.update()


    def creat_x(self,pos,preview_flag=0):
        if preview_flag:
            color='red'
        else:
            color='black'
        origin = np.array([20, 20])
        # creat x
        x_center = origin + [UNIT*pos[0],UNIT*pos[1]]
        self.x_pieces=self.canvas.create_polygon(
            x_center[0] - 11, x_center[1] - 15,
            x_center[0] + 15, x_center[1] + 11,
            x_center[0] + 11, x_center[1] + 15,
            x_center[0] - 15, x_center[1] - 11,
            fill=color
        )
        self.x_pieces=self.canvas.create_polygon(
            x_center[0] + 11, x_center[1] - 15,
            x_center[0] - 15, x_center[1] + 11,
            x_center[0] - 11, x_center[1] + 15,
            x_center[0] + 15, x_center[1] - 11,
            fill=color
        )
        self.canvas.update()


    def reset(self):
        # create grids
        print('reset')
        self.chessboard=[[0,0,0],[0,0,0],[0,0,0]]
        for i in self.canvas.find_all():
            self.canvas.delete(i)
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_W * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

def update():
    env.reset()

if __name__ == '__main__':
    env = Maze()
    env.after(100, update)
    env.mainloop()
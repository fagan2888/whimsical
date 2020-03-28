from tkinter import *
root = Tk()
def printCoords(event):
    print(event.x,event.y)
# 创建第一个Button,并将它与左键移动事件绑定
bt1 = Button(root,text = 'leftmost button')
bt1.bind('<B1-Motion>',printCoords)

# 创建二个Button，并将它与中键移动事件绑定
bt2 = Button(root,text = 'middle button')
bt2.bind('<B2-Motion>',printCoords)

# 创建第三个Button，并将它与右击移动事件绑定
bt3 = Button(root,text = 'rightmost button')
bt3.bind('<B3-Motion>',printCoords)


bt1.grid()
bt2.grid()
bt3.grid()

root.mainloop()
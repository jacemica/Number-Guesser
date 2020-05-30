from tkinter import *

def draw(event):
    color='black'
    x1, y1 = (event.x-1), (event.y-1)
    x2, y2 = (event.x+1), (event.y+1)
    c.create_oval(x1,y1,x2,y2, fill=color, width=5)

def end(event):
    print('test')



root = Tk()
c = Canvas(root, height=500, width=500, bg='white')
c.pack()
c.bind('<ButtonRelease-1>', end)
c.bind('<B1-Motion>', draw)

root.mainloop()
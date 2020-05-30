from tkinter import *
from PIL import Image, ImageDraw


size = 28

def draw(event):
    color='black'
    x1, y1 = (event.x-1), (event.y-1)
    x2, y2 = (event.x+1), (event.y+1)
    c.create_oval(x1,y1,x2,y2, fill=color, width=5)
    blank.arc([x1,y1,x2,y2], 0, 90, fill=color, width=500)

def end(event):
    filename = "myNum.jpg"
    myImage.save(filename)
    print("image saved")

myArray = [[]] * size
for i in myArray:
    i.append(0)

root = Tk()
c = Canvas(root, height=560, width=560, bg='white')
c.pack()

myImage = Image.new("RGB", (560, 560), 'white')
blank = ImageDraw.Draw(myImage)

c.bind('<ButtonRelease-1>', end)
c.bind('<B1-Motion>', draw)

root.mainloop()
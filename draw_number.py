from tkinter import *
import tensorflow as tf
from tensorflow import keras
from PIL import Image, ImageDraw
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import numpy as np
from numpy import asarray
from matplotlib import image, pyplot

size = 28
data = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = data.load_data()
x_test = keras.utils.normalize(x_test, axis=1)

def draw(event):
    color='black'
    x1, y1 = (event.x-1), (event.y-1)
    x2, y2 = (event.x+1), (event.y+1)
    c.create_rectangle(x1,y1,x2,y2, fill=color, width=10)
    blank.rectangle([x1-3,y1-3,x2+3,y2+3], fill=color, width=10)

def end(event):
    filename = "myNum.jpg"
    myImage.save(filename)
    print("image saved")

    img = load_img("myNum.jpg", color_mode="grayscale", target_size=(28, 28))
    img = img_to_array(img)
    img = img.reshape(28, 28)
    img = img.astype('float32')
    img = img/255.0
    
    for i in range(len(img)):
        for j in range(len(img[i])):
            if img[i][j] == 1:
                img[i][j] = 0
            else:
                img[i][j] = 1

    x_test[0] = img
    predictModel(x_test)

def predictModel(data):
    model = tf.keras.models.load_model('numbers.model')
    prediction = model.predict(data)
    p = np.argmax(prediction[0])
    print(p)
    pd = "I predict: " + str(p)
    pyplot.imshow(data[0])
    pyplot.suptitle(pd, fontsize=14)
    pyplot.text(0, 1, pd)
    pyplot.show()

if __name__ == "__main__":
    root = Tk()
    c = Canvas(root, height=200, width=200, bg='white')
    c.pack()

    myImage = Image.new("RGB", (200, 200), 'white')
    blank = ImageDraw.Draw(myImage)

    root.bind('<Return>', end)
    c.bind('<B1-Motion>', draw)

    root.mainloop()
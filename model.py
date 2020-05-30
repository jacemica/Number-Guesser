import tensorflow as tf
from tensorflow import keras 
import numpy as np 
import matplotlib.pyplot as plt

data = keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = data.load_data()

x_train = keras.utils.normalize(x_train, axis=1)
x_test = keras.utils.normalize(x_test, axis=1)

for train in range(len(x_train)):
    for row in range(28):
        for x in range(28):
            if x_train[train][row][x] != 0:
                x_train[train][row][x] = 1

print(x_train[0])
plt.imshow(x_train[0])
plt.show()

# model = keras.models.Sequential()
# model.add(keras.layers.Flatten())
# model.add(keras.layers.Dense(128, activation=tf.nn.relu))
# model.add(keras.layers.Dense(128, activation=tf.nn.relu))
# model.add(keras.layers.Dense(10, activation=tf.nn.softmax))

# model.compile(optimizer='adam',
#             loss='sparse_categorical_crossentropy',
#             metrics=['accuracy'])

# model.fit(x_train, y_train, epochs=3)



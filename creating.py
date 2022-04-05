from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout, Conv2D, MaxPooling2D, Flatten
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
batch_size = 1
epochs = 20
img_width, img_height = 9, 9
DATA_DIR_TRAIN = "C:/Users/Adrian/Desktop/keras/train"
DATA_DIR_TEST = "C:/Users/Adrian/Desktop/keras/test"
training_data = []
testing_data = []

def prepare(filepath):
    IMG_SIZE = 9
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

def create_training_data():
    path = os.path.join(DATA_DIR_TRAIN);
    i =0
    for img in os.listdir(path):
        result = np.zeros(10)
        result[i]=1
        img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
        training_data.append([img_array/255.0,result])
        i+=1
        if i ==10:
            i=0
def create_testing_data():
    path = os.path.join(DATA_DIR_TEST);
    i =0
    for img in os.listdir(path):
        result = np.zeros(10)
        result[i]=1
        img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
        testing_data.append([img_array/255.0,result])
        i+=1
        if i ==10:
            i=0


create_training_data()
create_testing_data()

x_train = []
y_train = []

for sample, label in training_data:
    x_train.append(sample)
    y_train.append(label)
x_train = np.array(x_train).reshape(-1,img_width,img_height,1)
y_train = np.array(y_train)

x_test = []
y_test = []

for sample, label in testing_data:
    x_test.append(sample)
    y_test.append(label)
x_test = np.array(x_test).reshape(-1,img_width,img_height,1)
y_test = np.array(y_test)
print(y_test)


model = Sequential()
model.add(Flatten(input_shape =(9,9)))
model.add(Dense(32, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

model.fit(x_train, y_train,batch_size=batch_size,epochs=epochs,validation_data=(x_test, y_test))

score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
print("Saving model...")
model.save("Model.h5")
print("Done.")



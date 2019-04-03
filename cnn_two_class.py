

from keras.layers import Dense, Dropout, Flatten, Activation
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.models import Sequential
import pandas as pd
from keras.utils import np_utils
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from PIL import Image
from keras import backend as K


img_width, img_height = 150, 150

train_data_dir = r'C:\Users\andre\Desktop\498B\498Bdata\Training'
validation_data_dir = r'C:\Users\andre\Desktop\498B\498Bdata\Validation'
nb_train_samples = 280
nb_validation_samples = 20
epochs = 7
batch_size = 12

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)
  
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples // batch_size)


model.save_weights('first_try.h5')
model.save('ECE498B.model')
test_image_path = r'C:\Users\andre\Desktop\498B\498Bdata\Validation\Class1\BloodImage_00361.jpg'

"""
This code is how you can test an individual image to see what prediction you obtain
"""
image_test = load_img(test_image_path, target_size = (150,150))
image_test_array = img_to_array(image_test)
image_test_array = np.expand_dims(image_test_array,axis=0)


prediction = model.predict_classes(image_test_array)




# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


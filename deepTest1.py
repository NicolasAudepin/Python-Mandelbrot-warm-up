# https://pythonprogramming.net/introduction-deep-learning-python-tensorflow-keras/
# j'ai suivi ce tuto à peu près à la lettre



import tensorflow as tf
import tensorflow.keras as keras
import numpy as np 
import matplotlib.pyplot as plt
<<<<<<< HEAD
#print(tf.__version__)
print("imported")
=======
print("version")
print(tf.__version__)

>>>>>>> ec89198a3693d73dd8ca0020a4d7dfe5c008c3da

np.random.seed(123) #pour avoir une seed fixe

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten #ce sont des composants des machines 
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils

mnist= tf.keras.datasets.mnist #les data du test
(xtr,ytr),(xte,yte)= mnist.load_data() # the tr are for training and the te are for testing
print("testing size :",yte.size)
print("training size:", ytr.size)
xtr = tf.keras.utils.normalize(xtr,axis = 1) #put velues between 0 and 1 instead of 0 and 255
xte = tf.keras.utils.normalize(xte,axis = 1)

model = tf.keras.models.Sequential() #basic feed foward model
model.add(tf.keras.layers.Flatten()) # on transforme la matrice en une grande matric collone mais je sais pas pourquoi
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(8, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))#la sortie de taille dix car y a dix chiffres
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(xtr, ytr, epochs=4)
print(ytr)
print("testing time !!")
val_loss, val_acc = model.evaluate(xte, yte)  # evaluate the out of sample data with model
print("loss",val_loss)  # model's loss (error)
print("accuracy",val_acc)  # model's accurac


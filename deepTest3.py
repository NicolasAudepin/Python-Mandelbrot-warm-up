import tensorflow as tf 
print("imported TF")
from tensorflow.keras.models import Sequential
print("imported keras.models")
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
print("imported keras.layers")
import pickle 

print("imported the stuff")

pickle_in = open("XDognCat.pickle","rb")
X= pickle.load(pickle_in)
pickle_in = open("yDognCat.pickle","rb")
y= pickle.load(pickle_in)

X= X/255.0 # normalising the dataset 
print("got the normalized dataset")
#print(X[6])
#print(y)

model = Sequential()
layer_List =[
    Conv2D(128 , (3,3), input_shape = X.shape[1:]),
    Activation("relu"),
    MaxPooling2D(pool_size = (2,2)),

    Conv2D(64 , (3,3)),
    Activation("relu"),
    MaxPooling2D(pool_size = (2,2)),

    Conv2D(64 , (3,3)),
    Activation("relu"),
    MaxPooling2D(pool_size = (2,2)),

    Flatten(),
    Dense(32),
    Activation("relu"),
    Dense(1),
    Activation('sigmoid')
    ]

for layer in layer_List:
    model.add(layer)

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
print("model compiled")
print("***fitting session starts now***")
model.fit(X, y, batch_size=16, epochs=3, validation_split=0.3)

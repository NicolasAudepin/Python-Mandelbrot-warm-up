#https://pythonprogramming.net/loading-custom-data-deep-learning-python-tensorflow-keras/

import numpy as np 
print("imported numpy")
import matplotlib.pyplot as plt
print("imported pyplot") 
import os
print("imported os")
import cv2
print("imported cv2")
import random
print("imported random")
from tqdm import tqdm
print("imported tqdm")
import pickle
print("imported pickle")

dataDirectory = "C:/Users/AUDEPIN/Documents/DataSet/training_set" #la dedans j'ai des dossiers contenant des milliers de photos de chat et de chiens
print(dataDirectory)
categorie_list = ["Dog","Cat"]

training_data_array=[]

img_size = 30 #the size at witch we will treat the pictures to make them less difficult to process

def create_data_array():

	
	for categorie in categorie_list:
		nb_erreur = 0
		class_index = categorie_list.index(categorie)
		thepath = os.path.join(dataDirectory,categorie)#on créé un path vers les categories du data set
		print(thepath)
		for imgname in tqdm(os.listdir(thepath)):
			try:
				imgpath = os.path.join(thepath,imgname)
				pix_array = cv2.imread(imgpath,cv2.IMREAD_GRAYSCALE) #marche quand même
				val_array = cv2.resize(pix_array,(img_size,img_size))
				training_data_array.append([val_array,class_index])
				#plt.imshow(val_array, cmap='gray')
				#plt.show()
			except Exception as e:
				nb_erreur +=1
		print("nombre d'image qui n'on pas pu etre lue:")
		print(nb_erreur)
	print("training data size:")
	print(len(training_data_array))
		
create_data_array()
random.shuffle(training_data_array)

print("creating X and y")
X = []
y = []
for features,label in training_data_array:
    X.append(features)
    y.append(label)
X = np.array(X).reshape(-1, img_size, img_size, 1)

print(X[0].reshape(-1, img_size, img_size, 1))
print(y)
#print(training_data_array[200])


pickle_out = open("XDognCat.pickle","wb")
pickle.dump(X, pickle_out)
pickle_out.close()
pickle_out = open("yDognCat.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()


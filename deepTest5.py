#https://machinelearningmastery.com/sequence-classification-lstm-recurrent-neural-networks-python-keras/

import numpy
#from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import os
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
print("stuff imported")
# fix random seed for reproducibility
numpy.random.seed(7)

categories = ["pos","neg"]
path = "C:/Users/AUDEPIN/Documents/DataSet/aclImdb-movie-review/train"

dim = 32
article_length = 500
vocad_size = 500

for cat in categories:
    y = categories.index(cat) 
    file_path = os.path.join(path,cat)
    

print(path)
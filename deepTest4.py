# https://machinelearningmastery.com/use-word-embedding-layers-deep-learning-keras/
from numpy import array
from numpy import asarray
from numpy import zeros
print("numpy imported")
from keras.preprocessing.text import one_hot
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Embedding
print("keras stuff inported")

# define documents
docs = ['Well done!',
		'Good work',
		'Great effort',
		'nice work',
		'Excellent!',
		'Weak',
		'Poor effort!',
		'not good',
		'poor work',
		'Could have done better.']
# define class labels
labels = array([1,1,1,1,1,0,0,0,0,0])

vocab_size =  50
maxlength = 4
encoded_docs = [one_hot(comment , vocab_size) for comment in docs]  
print(encoded_docs)

padded_docs = pad_sequences(encoded_docs, maxlen =maxlength, padding = 'post') # post signifie qu'on met les zeros après
print(padded_docs)

model = Sequential()
model.add(Embedding(input_dim = vocab_size, output_dim = 8, input_length = maxlength))
model.add(Flatten())
model.add(Dense(1, activation = "sigmoid"))
model.compile(optimizer = "adam",loss = "binary_crossentropy", metrics = ["accuracy"])
print(model.summary())


model.fit(padded_docs,labels,epochs = 105,verbose = 0)
loss, accuracy = model.evaluate(padded_docs, labels, verbose=0)
print('Accuracy: %f' % (accuracy*100))
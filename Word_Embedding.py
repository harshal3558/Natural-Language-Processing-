## Creating Word Embedding Layer

from tensorflow.keras.preprocessing.text import one_hot

sent=[  'the glass of milk',
     'the glass of juice',
     'the cup of tea',
    'I am a good boy',
     'I am a good developer',
     'understand the meaning of words',
     'your videos are good']

sent

voc_size = 500

onehot_repr=[one_hot(words,voc_size) for words in sent] 
print(onehot_repr)

# Word Embedding Representation

from tensorflow.keras.layers import Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential

import numpy as np

## pre padding
sent_length=8
embedded_docs=pad_sequences(onehot_repr,padding='pre',maxlen=sent_length)
print(embedded_docs)

## 10 feature dimensions
dim=10

model=Sequential()
model.add(Embedding(voc_size,10,input_length=sent_length))
model.compile('adam','mse')

model.summary()

##'the glass of milk',
embedded_docs[0]

model.predict(embedded_docs[0])

print(model.predict(embedded_docs))

embedded_docs[0]

print(model.predict(embedded_docs)[0])
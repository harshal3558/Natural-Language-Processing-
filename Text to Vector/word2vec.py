# """Open colab """
# import nltk
# #nltk.download('stopwords')
# nltk.download('punkt')
# from nltk.corpus import stopwords
# import re


# para = "In Harry world fate works not only through powers and objects such as prophecies, the Sorting Hat, wands, and the Goblet of Fire, but also through people. Repeatedly, other characters decide Harry future for him, depriving him of freedom and choice. For example, before his eleventh birthday, the Dursleys control Harry life, keeping from him knowledge of his past and understanding of his identity (Sorcerer 49). In Harry Potter and the Chamber of Secrets, Dobby repeatedly assumes control over events by intercepting Ron and Hermione letters during the summer; by sealing the barrier to Platform  causing Harry to miss the Hogwarts Express; and by sending a Bludger after Harry in a Quidditch match, breaking his wrist. Yet again, in Harry Potter and the Prisoner of Azkaban, many adults intercede while attempting to protect Harry from perceived danger, as Snape observes: Everyone from the Minister of Magic downward has been trying to keep famous Harry Potter safe from Sirius Black (284). All these characters, as enactors of fate, unknowingly drive Harry toward his destiny by attempting to control or to direct his life, while themselves controlled and directed by fate."

# # sentence tokenize
# sent = nltk.sent_tokenize(para)
# #print(sent)

# # stemming
# from nltk.stem import PorterStemmer
# stemmer = PorterStemmer()

# # stemming
# corpus = []
# for i in range(len(sent)):
#     review = re.sub('^a-zA-Z',' ',sent[i])
#     review = review.lower()
#     review = review.split()
#     review = [stemmer.stem(word) for word in review if word not in set(stopwords.words('english'))]
#     review = ' '.join(review)
#     corpus.append(review)

# #print(corpus)

# import gensim
# from sklearn.feature_extraction.text import CountVectorizer
# cv = CountVectorizer().fit_transform(corpus)
# print(cv[0].toarray())

import gensim.downloader as api
wv = api.load('word2vec-google-news-300')
vec_king = wv['king']
vec_king



from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()

corpus = []
for i in range(0, len(messages)):
    review = re.sub('[^a-zA-Z]', ' ', messages['message'][i])
    review = review.lower()
    review = review.split()
    
    review = [lemmatizer.lemmatize(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)


from nltk import sent_tokenize
from gensim.utils import simple_preprocess

corpus[0]
words=[]
for sent in corpus:
    sent_token=sent_tokenize(sent)
    for sent in sent_token:
        words.append(simple_preprocess(sent))
words


## Word2Vec model from scratch

import gensim
### Lets train Word2vec from scratch
model=gensim.models.Word2Vec(words,window=5,min_count=2)
model.wv.index_to_key

model.corpus_count
model.epochs
model.wv.similar_by_word('kid')
model.wv['kid'].shape



# Average Word2Vec


def avg_word2vec(doc):
    # remove out-of-vocabulary words
    #sent = [word for word in doc if word in model.wv.index_to_key]
    #print(sent)
    
    return np.mean([model.wv[word] for word in doc if word in model.wv.index_to_key],axis=0)
                #or [np.zeros(len(model.wv.index_to_key))], axis=0)
        
from tqdm import tqdm
words[73]
type(model.wv.index_to_key)


#apply for the entire sentences
X=[]
for i in tqdm(range(len(words))):
    print("Hello",i)
    X.append(avg_word2vec(words[i]))

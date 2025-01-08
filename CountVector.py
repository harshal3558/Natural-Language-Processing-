import nltk
#nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
nltk.download('wordnet')
import re

para = "In Harry world fate works not only through powers and objects such as prophecies, the Sorting Hat, wands, and the Goblet of Fire, but also through people. Repeatedly, other characters decide Harry future for him, depriving him of freedom and choice. For example, before his eleventh birthday, the Dursleys control Harry life, keeping from him knowledge of his past and understanding of his identity (Sorcerer 49). In Harry Potter and the Chamber of Secrets, Dobby repeatedly assumes control over events by intercepting Ron and Hermione letters during the summer; by sealing the barrier to Platform  causing Harry to miss the Hogwarts Express; and by sending a Bludger after Harry in a Quidditch match, breaking his wrist. Yet again, in Harry Potter and the Prisoner of Azkaban, many adults intercede while attempting to protect Harry from perceived danger, as Snape observes: Everyone from the Minister of Magic downward has been trying to keep famous Harry Potter safe from Sirius Black (284). All these characters, as enactors of fate, unknowingly drive Harry toward his destiny by attempting to control or to direct his life, while themselves controlled and directed by fate."

# sentence tokenize
sent = nltk.sent_tokenize(para)
print(sent)

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

corpus = []
for i in range(len(sent)):
    review = re.sub('^a-zA-Z',' ',sent[i])
    review = review.lower()
    review = review.split()
    review = [lemmatizer.lemmatize(word) for word in review if word not in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

print(corpus)

# from sklearn.feature_extraction.text import CountVectorizer
# cv = CountVectorizer(binary=True)
# cv.fit_transform(corpus).toarray()

# from sklearn.feature_extraction.text import CountVectorizer
# cv = CountVectorizer(binary=True, ngram_range=(2,2))
# X = cv.fit_transform(corpus) #.toarray()
# print(cv.vocabulary_)

# from sklearn.feature_extraction.text import CountVectorizer
# cv = CountVectorizer()
# cv.fit_transform(corpus).toarray()
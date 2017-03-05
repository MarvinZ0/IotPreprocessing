
# return the text without stopwords
def CleanStw(text):
    from nltk.corpus import stopwords
    import re
    StpWds = stopwords.words('english')
    text = ' '.join([word for word in re.sub("[^A-Za-z0-9_' ]","",text).lower().split() if word not in StpWds])
    return text

def Stemming(text):
    from nltk.stem.snowball import SnowballStemmer
    stemmer = SnowballStemmer("english")
    text = ' '.join([stemmer.stem(word) for word in text.split(" ")])
    return text

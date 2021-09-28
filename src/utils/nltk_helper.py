import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

stop_words = set(stopwords.words('english'))
regex_tokenizer = RegexpTokenizer('\\W+', gaps = True)

def get_tokens_from_sentence(sentence):
    """
    generate tokens from a sentence and filter stop words
    """
    word_tokens = regex_tokenizer.tokenize(sentence)
    filtered_word_tokens = [w.lower() for w in word_tokens if not w.lower() in stop_words]
    return filtered_word_tokens

def extract_keywords_from_sentence(sentence, list_keywords):
    """
    find the list of keywords which are mentioned by the sentence
    """
    word_tokens = get_tokens_from_sentence(sentence)
    keywords_mentioned = [w for w in list_keywords if w.lower() in word_tokens]
    return keywords_mentioned    

import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


def stem_text(text):
    """
    Perform stemming on the input text.

    Args:
    - text (str): The input text to be stemmed.

    Returns:
    - str: The input text with words stemmed.
    """
    stemmer = PorterStemmer()
    words = nltk.word_tokenize(text)
    stemmed_words = [stemmer.stem(word) for word in words]
    return ' '.join(stemmed_words)



def lemmatize_text(text):
    """
    Lemmatize words in the input text.

    Args:
    - text (str): The input text to be lemmatized.

    Returns:
    - str: The input text with words lemmatized.
    """
    lemmatizer = WordNetLemmatizer()
    words = nltk.word_tokenize(text)
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(lemmatized_words)



def tokenize_text(text):
    """
    Tokenize the input text into words.

    Args:
    - text (str): The input text to be tokenized.

    Returns:
    - list of str: List of tokens (words) from the input text.
    """
    return word_tokenize(text)

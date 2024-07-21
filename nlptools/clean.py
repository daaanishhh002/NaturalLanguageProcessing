import re
import emoji
import string
import nltk
from autocorrect import Speller
from nltk.corpus import stopwords



def remove_emojis(text):
    """
    Remove emojis from the input text.

    Args:
    - text (str): The input text possibly containing emojis.

    Returns:
    - str: The input text with emojis removed.
    """
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"
                               u"\U0001F300-\U0001F5FF"
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1E0-\U0001F1FF"
                               u"\U00002500-\U00002BEF"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)



def translate_emojis(text):
    """
    Replace emojis in the input text with their meanings.

    Args:
    - text (str): The input text possibly containing emojis.

    Returns:
    - str: The input text with emojis replaced by their meanings.
    """
    def replace(match):
        emoji_char = match.group(0)
        try:
            emoji_meaning = emoji.demojize(emoji_char)
        except KeyError:
            return emoji_char
        return emoji_meaning.replace(":", " ").replace("_", " ")

    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"
                               u"\U0001F300-\U0001F5FF"
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1E0-\U0001F1FF"
                               u"\U00002500-\U00002BEF"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f\u3030"
                               "]+", flags=re.UNICODE)
    
    return emoji_pattern.sub(replace, text)



def remove_html_tags(text):
    """
    Remove HTML tags from the input text.

    Args:
    - text (str): The input text possibly containing HTML tags.

    Returns:
    - str: The input text with HTML tags removed.
    """
    html_pattern = re.compile('<.*?>')
    return re.sub(html_pattern, '', text)



def remove_urls(text):
    """
    Remove URLs from the input text.

    Args:
    - text (str): The input text possibly containing URLs.

    Returns:
    - str: The input text with URLs removed.
    """
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return re.sub(url_pattern, '', text)



def remove_punctuations(text):
    """
    Remove punctuations from the input text.

    Args:
    - text (str): The input text possibly containing punctuations.

    Returns:
    - str: The input text with punctuations removed.
    """
    return text.translate(str.maketrans('', '', string.punctuation))



def remove_numbers(text):
    """
    Remove numbers from the input text.

    Args:
    - text (str): The input text possibly containing numbers.

    Returns:
    - str: The input text with numbers removed.
    """
    return re.sub(r'\d+', '', text)



def remove_special_characters(text):
    """
    Remove special characters (non-alphanumeric) from the input text.

    Args:
    - text (str): The input text possibly containing special characters.

    Returns:
    - str: The input text with special characters removed.
    """
    return re.sub(r'[^A-Za-z0-9\s]', '', text)



def remove_mentions(text):
    """
    Remove @mentions (Twitter-like usernames) from the input text.

    Args:
    - text (str): The input text possibly containing @mentions.

    Returns:
    - str: The input text with @mentions removed.
    """
    return re.sub(r'@[a-zA-Z0-9_]+', '', text)



def expand_chat_words(text, chat_words_dict):
    """
    Expand chat words, acronyms, and slangs in the input text using a provided dictionary.

    Args:
    - text (str): The input text possibly containing chat words.
    - chat_words_dict (dict): A dictionary mapping chat words (keys) to their expanded forms (values).

    Returns:
    - str: The input text with chat words expanded.

    Example usage:
    >>> chat_words_dict = {
    >>>     "lol": "laughing out loud",
    >>>     "brb": "be right back",
    >>>     "np": "no problem"
    >>> }
    >>> text_with_chat_words = "lol, brb, np"
    >>> expanded_text = expand_chat_words(text_with_chat_words, chat_words_dict)
    >>> print(expanded_text)
    >>> # Output: "laughing out loud, be right back, no problem"
    """
    words = text.split()
    return ' '.join(chat_words_dict.get(word.lower(), word) for word in words)



def correct_spelling(text):
    """
    Correct spelling mistakes in the input text.

    Args:
    - text (str): The input text possibly containing spelling mistakes.

    Returns:
    - str: The input text with spelling mistakes corrected.
    """
    spell = Speller(lang='en')
    return spell(text)



def remove_stopwords(text):
    """
    Remove stop words from the input text.

    Args:
    - text (str): The input text possibly containing stop words.

    Returns:
    - str: The input text with stop words removed.
    """
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)


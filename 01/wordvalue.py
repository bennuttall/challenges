from data import DICTIONARY, LETTER_SCORES

def foo(word):
    return all(letter.upper() in LETTER_SCORES for letter in word)

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as f:
        return list(filter(foo, f.read().split()))

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES[letter.upper()] for letter in word)

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    word_values = {calc_word_value(word): word for word in words}
    return word_values[max(word_values)]


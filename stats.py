"""

Contains functions that collect certain statistical
characteristics of the text that are necessary in order
to calculate a readability index by different formulas.
All the functions can be used for other NLP tasks as well.

"""

from spacy import load  # load a spaCy language models
from string import punctuation  # string of characters which are considered punctuation characters
from langdetect import detect  # identify language of the piece of text
from re import fullmatch
from csv import reader
import textstat  # used in order to analyze syllabic contents of English words


def break_sentences(text):
    """Return a list of sentences from the text (applicable
    to texts in Russian and English languages)."""
    # identify the language of the text and use the corresponding spaCy model
    if detect(text) == 'en':
        nlp = load('en_core_web_sm')
        doc = nlp(text)
    elif detect(text) == 'ru':
        nlp = load('ru_core_news_sm')
        doc = nlp(text)
    sentence_list = list(doc.sents)
    return sentence_list


def sentence_count(text):
    """Return a number of sentences in the piece of text"""
    return len(break_sentences(text))


def get_words(text):
    """Return a list of words from the text (excluding numbers)"""
    word_list = [word.lower().strip(punctuation) for word in text.split()]
    # create a list of words in lower case and remove the punctuation
    # find numbers in the word list using re.fullmatch and remove them
    for word in word_list:
        if fullmatch('\d*', word):
            word_list.remove(word)
    return word_list


def get_lemmas(text):  # lemmas are needed for Dale-Chall formula
    """Return a list of lemmas from the text using spaCy model"""
    if detect(text) == 'en':
        nlp = load('en_core_web_sm')
    elif detect(text) == 'ru':
        nlp = load('ru_core_news_sm')
    # use words instead of the initial text to prevent punctuation getting on the list
    doc = nlp(' '.join(get_words(text)))
    lemma_list = [token.lemma_ for token in doc if token.lemma_ not in punctuation]
    return lemma_list


def word_count(text):
    """Return a number of words in the piece of text"""
    return len(get_words(text))


def avg_sentence_length(text):
    """Return an average sentence length in words (i.e. words per sentence)"""
    length = word_count(text) / sentence_count(text)
    return length


def syllable_count(text):
    """Return a list containing number of syllables in every word in the piece of text"""
    syllables_in_word = []
    word_list = get_words(text)
    # identify the language of the text and use a corresponding module
    if detect(text) == 'en':
        for word in word_list:
            syllables_in_word.append(textstat.syllable_count(word))
    elif detect(text) == 'ru':
        # count syllables in Russian words by counting vowels
        for word in word_list:
            word_syllable_count = 0
            if len(word) > 1:
                for letter in word:
                    if fullmatch('[уеыаоэяию]', letter):
                        word_syllable_count += 1
            else:
                word_syllable_count += 1
            syllables_in_word.append(word_syllable_count)
    return syllables_in_word


def hard_words(text):
    """Return a list of words that are not stop words and contain more than 2 syllables
    for English words and more than 4 syllable for Russian words"""
    hard_word_list = []
    nlp = load('en_core_web_sm')
    words = get_words(text)
    stop_words_english = nlp.Defaults.stop_words
    stop_words_russian = []
    with open('Stop_words_Russian.csv') as csv_file:
        data = reader(csv_file, delimiter=';')
        for row in data:
            stop_words_russian.append(row[0])
    # add words that are not stop words and have certain amount of syllables to the list
    if detect(text) == 'en':
        hard_word_list = list(
            word for word in words if word not in stop_words_english and textstat.syllable_count(word) > 2)
    elif detect(text) == 'ru':
        counter = 0
        for word in words:
            if word not in stop_words_russian and syllable_count(text)[counter] > 4:
                hard_word_list.append(word)
            counter += 1
    return hard_word_list


def hard_words_count(text):
    """Return a number of hard words in the piece of text"""
    return len(hard_words(text))


def avg_word_syllable_length(text):
    """Return an average length of the word in syllables (i.e. syllables per word)"""
    syllable_total = 0
    for number in syllable_count(text):
        syllable_total += number
    word_length = syllable_total / word_count(text)
    return word_length


def letter_count(text):
    """Return a number of characters (excluding spaces and punctuation) in the piece of text"""
    count = 0
    for letter in text:
        if letter not in punctuation and letter != ' ':
            count += 1
    return count


def letter_per_100(text):
    """Return an average number of characters per 100 words"""
    count = (letter_count(text) / word_count(text)) * 100
    return count


def sentences_per_100(text):
    """Return an average number of sentences per 100 words"""
    count = (sentence_count(text) / word_count(text)) * 100
    return count


def dale_chall_hard_words(text):
    """Return a list of hard words that are not on a Dale-Chall list"""
    text_hard_words = []
    with open('Dale-Chall list.csv') as csv_file:
        data = reader(csv_file, delimiter=';')
        dale_chall_words = []
        for row in data:
            dale_chall_words.append(row[0])
    # use lemmas here in order to compare the initial word forms to words on the list
    for lemma in get_lemmas(text):
        if lemma not in dale_chall_words:
            text_hard_words.append(lemma)
    return text_hard_words


def dale_chall_hard_word_count(text):
    """Return a number of words that are not on a Dale-Chall list"""
    return len(dale_chall_hard_words(text))

"""

Contains different formulas that calculate a readability index.
Functions containing data on different readability indexes are present
here as well.

"""


from stats import *
from langdetect import detect


def flesch_index(text):
    """Return Flechs index of the given English or Russian text.
    Flesch index is calculated with the usage of
    average sentence length and average number of syllables per word """
    if detect(text) == 'en':
        index = round(
            206.835 - (1.015 * avg_sentence_length(text)) - (84.6 * avg_word_syllable_length(text)), 2)
        return index
    elif detect(text) == 'ru':
        index = round(
            206.835 - (1.3 * avg_sentence_length(text)) - (60.1 * avg_word_syllable_length(text)), 2)
        return index


def gunning_fog_index(text):
    """Return Gunning fog index of the given English or Russian text.
    Gunning fog index is calculated with the usage of
    average sentence length and the percentage of hard words (words that are not stop-words
    and consist of more than 2 syllables for English language and 4 syllables for Russian language)"""
    if detect(text) == 'en':
        index = round(
            0.4 * (avg_sentence_length(text) + (hard_words_count(text) * 100 / word_count(text))))
        return index
    elif detect(text) == 'ru':
        index = round(0.4 * ((0.78 * avg_sentence_length(text)) + (
                    hard_words_count(text) * 100 / word_count(text))))
        return index


def c_l_index(text):
    """Return Coleman-Liau index of the given English or Russian text.
    Coleman_Liau index is calculated with the usage of average number of letters per 100 words
    and average number of sentences per 100 words"""
    index = round(0.0588 * letter_per_100(text) - 0.296 * sentences_per_100(text) - 15.8)
    # warn about inaccuracy when formula is applied to a non-English text and proceed
    if detect(text) != 'en':
        print('Warning! Coleman-Liau formula was designed for English texts '
              'and might provide inaccurate results for texts in other languages.')
    return index


def dale_chall_index(text):
    """Return Dale-Chall index of the given English text.
    Dale-Chall index is calculated with the usage of average sentence length and percentage of hard words
    (words that are not on Dale-Chall familiar word list)."""
    if detect(text) == 'en':
        hard_word_percentage = (dale_chall_hard_word_count(text) / word_count(text)) * 100
        index = 0.1579 * hard_word_percentage + 0.0496 * avg_sentence_length(text)
        if hard_word_percentage > 5:
            index += 3.6365
        return round(index, 2)


def automated_readability_index(text):
    """Return Automated Readability Index of the given English text.
    Automated Readability Index is calculated with the usage of average number of characters per word
    and average number of words per sentence"""
    index = round(
        4.71 * (letter_count(text) / word_count(text)) + 0.5 * (avg_sentence_length(text)) - 21.43)
    # warn about inaccuracy when formula is applied to a non-English text and proceed
    if detect(text) != 'en':
        print('Warning! Automated Readability Index was designed for English texts '
              'and might provide inaccurate results for texts in other languages.')
    return index


def flesch_index_data(f_index):
    """Return data on Flesch index of the given English or Russian text"""
    # error message if input text is not in English or Russian
    if f_index is None:
        message_1 = 'Error! '
        message_2 = 'This formula works only with English or Russian texts.' \
                    'Make sure that input text is written in English or Russian and try again'
    else:
        message_1 = f"Flesch reading-ease score is {f_index}. "
        if f_index < 10:
            message_2 = 'School level of difficulty: professional. Extremely difficult to read.'
        elif f_index < 30:
            message_2 = 'School level of difficulty: college graduate. Very difficult to read.'
        elif f_index < 50:
            message_2 = 'School level of difficulty: college. Difficult to read.'
        elif f_index < 60:
            message_2 = 'School level of difficulty: 10th - 12th grade. Fairly difficult to read.'
        elif f_index < 70:
            message_2 = 'School level of difficulty: 8th - 9th grade. Plain language.'
        elif f_index < 80:
            message_2 = 'School level of difficulty: 7th grade. Fairly easy to read.'
        elif f_index < 90:
            message_2 = 'School level of difficulty: 6th grade. Easy to read.'
        else:
            message_2 = 'School level of difficulty: 5th grade. Very easy to read.'
    return message_1 + message_2 + '\n'


def gunning_fog_data(fog_index):
    """Return data on Gunning fog index of the given text."""
    # error message if input text is not in English or Russian
    if fog_index is None:
        message_1 = 'Error! '
        message_2 = 'This formula works only with English or Russian texts.' \
                    'Make sure that input text is written in English or Russian and try again'
    else:
        message_1 = f"Gunning fog index is {fog_index}. "
        message_2 = ''
        if fog_index <= 6:
            message_2 = 'School level of difficulty: 6th grade or lower.'
        elif fog_index == 7:
            message_2 = 'School level of difficulty: 7th grade.'
        elif fog_index == 8:
            message_2 = 'School level of difficulty: 8th grade.'
        elif fog_index == 9:
            message_2 = 'School level of difficulty: high school freshman.'
        elif fog_index == 10:
            message_2 = 'School level of difficulty: high school sophomore.'
        elif fog_index == 11:
            message_2 = 'School level of difficulty: high school junior.'
        elif fog_index == 12:
            message_2 = 'School level of difficulty: high school senior.'
        elif fog_index == 13:
            message_2 = 'School level of difficulty: college freshman.'
        elif fog_index == 14:
            message_2 = 'School level of difficulty: college sophomore.'
        elif fog_index == 15:
            message_2 = 'School level of difficulty: college junior'
        elif fog_index == 16:
            message_2 = 'School level of difficulty: college senior.'
        elif fog_index >= 17:
            message_2 = 'School level of difficulty: college graduate.'
    return message_1 + message_2 + '\n'


def cl_data(cl_index):
    """Return data on Gunning fog index of the given text."""
    message_1 = f"Coleman-Liau index is {cl_index}. "
    message_2 = ''
    if cl_index <= 6:
        message_2 = 'School level of difficulty: 6th grade or lower.'
    elif cl_index == 7:
        message_2 = 'School level of difficulty: 7th grade.'
    elif cl_index == 8:
        message_2 = 'School level of difficulty: 8th grade.'
    elif cl_index == 9:
        message_2 = 'School level of difficulty: high school freshman.'
    elif cl_index == 10:
        message_2 = 'School level of difficulty: high school sophomore.'
    elif cl_index == 11:
        message_2 = 'School level of difficulty: high school junior.'
    elif cl_index == 12:
        message_2 = 'School level of difficulty: high school senior.'
    elif cl_index == 13:
        message_2 = 'School level of difficulty: college freshman.'
    elif cl_index == 14:
        message_2 = 'School level of difficulty: college sophomore.'
    elif cl_index == 15:
        message_2 = 'School level of difficulty: college junior'
    elif cl_index == 16:
        message_2 = 'School level of difficulty: college senior.'
    elif cl_index >= 17:
        message_2 = 'School level of difficulty: college graduate.'
    return message_1 + message_2 + '\n'


def dale_chall_data(dl_index):
    """Return data on Dale-Chall index of the given English text"""
    # error message when formula is applied to a non-English text
    if dl_index is None:
        message_1 = 'Error! '
        message_2 = 'This formula works only with English texts.' \
                    'Make sure that input text is an English text and try again!'
    else:
        message_1 = f"Dale–Chall readability score is {dl_index}: "
        if dl_index < 4.9:
            message_2 = 'easily understood by an average 4th-grade student or lower.'
        elif dl_index < 5.9:
            message_2 = 'easily understood by an average 5th or 6th-grade student.'
        elif dl_index < 6.9:
            message_2 = 'easily understood by an average 7th or 8th-grade student.'
        elif dl_index < 7.9:
            message_2 = '	easily understood by an average 9th or 10th-grade student.'
        elif dl_index < 8.9:
            message_2 = 'easily understood by an average 11th or 12th-grade student.'
        elif dl_index < 9.9:
            message_2 = 'easily understood by an average 13th to 15th-grade (college) student.'
        else:
            message_2 = 'understood by an average college graduate.'
    return message_1 + message_2 + '\n'


def automated_readability_data(ar_index):
    """Return data on Automated Readability Index of the given English text"""
    message_1 = f'Automated Readability Index is {ar_index}: '
    message_2 = ''
    if ar_index < 2:
        message_2 = 'understood by a 5-6-year-old child.'
    elif ar_index < 3:
        message_2 = 'understood by a 6-7-year-old child.'
    elif ar_index < 4:
        message_2 = 'understood by a 7-8-year-old child.'
    elif ar_index < 5:
        message_2 = 'understood by a 8-9-year-old child.'
    elif ar_index < 6:
        message_2 = 'understood by a 9-10-year-old child.'
    elif ar_index < 7:
        message_2 = 'understood by a 10-11-year-old child.'
    elif ar_index < 8:
        message_2 = 'understood by a 11-12-year-old child.'
    elif ar_index < 9:
        message_2 = 'understood by a 12-13-year-old person.'
    elif ar_index < 10:
        message_2 = 'understood by a 13-14-year-old person.'
    elif ar_index < 11:
        message_2 = 'understood by a 14-15-year-old person.'
    elif ar_index < 12:
        message_2 = 'understood by a 15-16-year-old person.'
    elif ar_index < 13:
        message_2 = 'understood by a 16-17-year-old person.'
    elif ar_index < 14:
        message_2 = 'understood by a 17-18-year-old person.'
    elif ar_index >= 14:
        message_2 = 'understood by a an adult.'
    return message_1 + message_2 + '\n'

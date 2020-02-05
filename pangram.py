import string

alphabet = set(string.ascii_lowercase)


def is_pangram(sentence):
    return set(sentence.lower()) >= alphabet

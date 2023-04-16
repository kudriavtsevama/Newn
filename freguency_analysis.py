from collections import Counter
from cipher import caeser_encrypt
from utilis import numeric
from utilis import rus


def hack(text):
    for i in text:
        if i.isalpha and i != ' ':
            if rus(i):
                return simple_hack_rus(text)
            else:
                return simple_hack_eng(text)


def simple_hack_eng(text2):  # работает, правда только если в тексте самая частая буква - e
    letters = []
    for i in text2:
        if i.isalpha and (i != ' '):
            letters.append(i)
    counter = (Counter(letters))
    e_ = counter.most_common()[0][0]
    return caeser_encrypt(text2, numeric((str(e_))) - numeric('e'), -1)


def simple_hack_rus(text2):  # работает, правда только если в тексте самая частая буква - о
    letters = []
    for i in text2:
        if i.isalpha and (i != ' '):
            letters.append(i)
    counter = (Counter(letters))
    o_ = counter.most_common()[0][0]
    return caeser_encrypt(text2, numeric((str(o_))) - numeric('o'), -1)
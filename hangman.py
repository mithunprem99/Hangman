import random


def get_random_word(wordfile = "/usr/share/dict/words"):
    candidate_words = []
    with open(wordfile) as f:
        for word in f:
            word = word.strip()
            if len(word) >= 6 and word.islower() and word.isalpha():
                candidate_words.append(word)
    word = random.choice(candidate_words)
    return word

def masked_word(guess_word,worng_guess):
    return '-'*len(guess_word)
       






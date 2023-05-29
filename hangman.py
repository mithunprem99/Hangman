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

def masked_word(word, guess):
    guess_word= []
    for i in word:
        if i in guess:
            guess_word.append(i)
        else:
            guess_word.append("-")
    return "".join(guess_word)

def check_game_win(word , guess):
    if word == guess:
        return "You Win!"
    else:
        return "You Lose!"


    
       






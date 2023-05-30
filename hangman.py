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

def get_partial_solution(word):
    return '-'*len(word)


# def check_game_loop(partial_word , word, guesses):
#     if partial_word != word:
#         return True
#     return False

# def check_game_loops(partial_word,word):
#     if partial_word != word:
#         return False

def user_input():
    return input("Your Guess").islower()



# def main():
#     random_word = get_random_word()
#     guesses = []
#     turns_left = 7
#     while True:
#         guess = user_input()

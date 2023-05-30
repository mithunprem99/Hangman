import random

Guessed_word = 0
Correct =1
Wrong = 2
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

def get_status(secret_word, guesses, turns_remaining):
    mask_word = masked_word(secret_word, guesses)
    guessed_letters = " ".join(guesses)
    return f"""Secret word:{mask_word}
Guesses : {guessed_letters}
Remaining turns : {turns_remaining}"""

def check_guesses(word, guesses, remaining_turns, new_guess):
    if new_guess in guesses:
        return Guessed_word, remaining_turns
    else:
        guesses.append(new_guess)
        if new_guess in word:
            return Correct, remaining_turns
        else:
            return Wrong, remaining_turns-1


# def game_over(word, guesses, remaining_turns):
#     if turns_remaining == 0:
#         return True, f"You lost! The word was {secret_word}"
#     masked = mask_word(secret_word, guesses)
#     if "-" in masked:
#         return False, None
#     else:
#         return True, f"You guessed it! The word was {secret_word}"


# def main():
#     random_word = get_random_word()
#     guesses = []
#     turns_left = 7
#     while True:
#         guess = user_input()

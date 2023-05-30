import os
import tempfile
import hangman


def test_select_random_word_min_length():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["cat\n","elephant\n","mouse\n","dog\n"])
    f.close()

    for _ in range(20):
        secret_word = hangman.get_random_word(name)
        assert secret_word == "elephant"

    os.unlink(name)

def test_select_random_word_no_non_alpha_chars():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["pine's\n","Dr.\n","Ångström\n","policeman\n"])
    f.close()

    # for _ in range(20):
    secret_word = hangman.get_random_word(name)
    assert secret_word == "policeman"

    os.unlink(name)

def test_select_random_word_no_capitals():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["Alexander\n","AMD\n","California\n","pelican\n"])
    f.close()

    for _ in range(20):
        secret_word = hangman.get_random_word(name)
        assert secret_word == "pelican"

    os.unlink(name)


def test_select_random_word_no_repetitions():
    secret_words = set()
    for _ in range(10):
        secret_words.add(hangman.get_random_word())
    assert len(secret_words) == 10
            
def test_masked_word_no_guesses():
    word = "elephant"
    assert hangman.masked_word(word,[])== '--------'

def test_masked_word_wrong_guess():
    word = "elephant"
    assert hangman.masked_word(word, ['x']) == '--------'

def test_masked_word_repeated_guess():
    word ='elephant'
    assert hangman.masked_word(word,['s', 's']) == '--------'

def test_masked_word_correct_guess():
    word = "elephant"
    assert hangman.masked_word(word, ["e","l" ,"p","h", "a",'n','t']) == "elephant"


def test_masked_word_repeated_letters():
    word = 'elephant'
    assert hangman,masked_word(word, ['e']) == 'e-e-----'

def test_get_status_basic():
    secret_word = "helicopter"
    guesses = ["c", "o", "x"]
    turns_remaining = 3

    assert hangman.get_status(secret_word, guesses, turns_remaining) == """Secret word:----co----
Guesses : c o x
Remaining turns : 3"""

def test_get_status_no_guesses():
    secret_word = "elephant"
    guesses = []
    turns_remaining = 7
    assert hangman.get_status(secret_word, guesses, turns_remaining) == """Secret word:--------
Guesses : 
Remaining turns : 7"""

def test_check_already_guessed():
    word = "elephant"
    guesses = ["e", "p"]
    remaining_turns = 5
    new_guess = "p"
    status, remaining_turns = hangman.check_guesses(word, guesses, 
                                            remaining_turns, 
                                            new_guess)
    assert status == hangman.Guessed_word
    assert remaining_turns == 5
    assert guesses == ["e", "p",]


def test_check_correct_word():
    word = "elephant"
    guesses = ["l", "t"]
    remaining_turns = 6
    new_guess = "a"
    status, remaining_turns = hangman.check_guesses(word, guesses, 
                                            remaining_turns, 
                                            new_guess)
    assert status == hangman.Correct
    assert remaining_turns == 6
    assert guesses == ["l", "t", "a"]

def test_check_wrong():
    word = "elephant"
    guesses = ["i", "t", "p"]
    remaining_turns = 6
    new_guess = "x"
    status, remaining_turns = hangman.check_guesses(word, guesses, 
                                            remaining_turns, 
                                            new_guess)
    assert status == hangman.Wrong
    assert remaining_turns == 5
    assert guesses == ["i", "t", "p", "x"]

def test_game_over_won():
    word = "elephant"
    guesses = ["e", "l", "e", "p", "h" ,"a" ,"n", "t"]
    remaining_turns = 5
    finished, message = hangman.game_over(word, guesses, remaining_turns)
    assert finished
    assert message == "You guessed it! The word was elephant"

def test_game_over_lost():
    word = "elephant"
    guesses = ["e", "l", "e", "p", "h", "a" , "n","t"]
    remaining_turns = 0
    finished, message = hangman.game_over(word, guesses, remaining_turns)
    assert finished
    assert message == "You lost! The word was elephant"
# def test_check_game_win():
#     word = 'elephant'
#     assert hangman.check_game_win(word, 'elephant') == 'You Win!'

# def test_check_game_win():
#     word = "elephant"
#     assert hangman.check_game_win(word, '_lephant') == 'You Lose!'

# # def test_user_guesses():
# #     word = 'elephant'
# #     assert 

# def test_partial_solution_input():
#     word = 'elephant'
#     assert hangman.get_partial_solution(word) == '--------'


# def test_check_game_next_turn():
#     word = 'elephant'
#     assert hangman.check_game_loop('_lephant', word, ['w', 'y']) == True

# def test_game_win():
#     word = 'elephant'
#     assert hangman.check_game_loop('elephant',word,['z',]) == False


# def test_game_out_of_turns():
#     # word = 'elephant'
#     assert hangman.check_game_loops('-leph-nt',['z','y','x','j','k','o','q','u']) == False

# # number of turns = 7
# # guesses
# #new_guesses



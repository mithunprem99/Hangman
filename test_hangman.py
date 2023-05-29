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

# def test_masked_word_repeated_letters():
#     assert
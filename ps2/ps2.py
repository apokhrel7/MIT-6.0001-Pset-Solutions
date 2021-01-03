# Problem Set 2, hangman.py
# Name: Anish Pokhrel
# Collaborators:
# Time spent:  # Started: Aug 5, 2020
# Finished: Aug 11, 2020

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "ps2_words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    word_length = []
    [word_length.append(i) for i in secret_word if i in letters_guessed]
    return len(word_length) == len(secret_word)

    # for i in secret_word:                               #Longer version
    #     if i in letters_guessed:
    #         word_length.append(i)
    # return len(word_length) == len(secret_word)


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    guessed_word_length = []
    [guessed_word_length.append(i) if i in letters_guessed else guessed_word_length.append("_") for i in secret_word]
    return ''.join(guessed_word_length)


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    alphabet = list(string.ascii_lowercase)
    alphabet_copy = alphabet[:]

    [alphabet.remove(char) for char in alphabet_copy if char in letters_guessed]
    return ' '.join(alphabet)


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    """
    guesses = 6
    warnings = 3

    print("\n---------------------------------------------")
    print('Welcome to the "Hangman" game!!!')
    print("I'm thinking of a word that is {} letters long".format(len(secret_word)))
    print("---------------------------------------------")
    print("\nYou have {}".format(warnings), "warnings" if warnings > 1 else "warning", "left")

    letters_guessed = []

    while is_word_guessed(secret_word, letters_guessed) == False:

        print("You have {}".format(guesses), "guesses" if guesses > 1 else "guess", "left: ")
        print("Available letters: ", get_available_letters(letters_guessed))
        print("Letters already guessed: ", ' '.join(letters_guessed))

        user_letters = str.lower(input("Please guess a letter: "))

        if user_letters in letters_guessed:
            if warnings >= 1:
                warnings -= 1
                print("##########################################################\n")
                print(
                    "Oops! You\'ve already guessed that letter. You have", warnings, "warning" if warnings == 1
                    else "warnings", "left:", get_guessed_word(secret_word, letters_guessed)
                )
                print("\n##########################################################")
            else:
                guesses -= 1
                print("##########################################################\n")
                print("Oops! You\'ve already guessed that letter. You have no warnings left, so you lose one guess:",
                      get_guessed_word(secret_word, letters_guessed)
                      )
                print("\n##########################################################")

            letters_guessed.append(user_letters)
        else:
            letters_guessed.append(user_letters)

            right = []
            wrong = []
            [right.append(i) if i in secret_word else wrong.append(i) for i in user_letters]

            for i in right:
                print("##########################################################\n")
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                print("\n##########################################################")
                break

            for i in wrong:
                if not str.isalpha(i) and warnings >= 1:
                    warnings -= 1
                    print("##########################################################\n")
                    print(
                        "Oops! That is not a valid letter. You have", warnings, "warning" if warnings == 1
                        else "warnings", "left:", get_guessed_word(secret_word, letters_guessed)
                    )
                    print("\n##########################################################")

                elif not str.isalpha(i) and warnings < 1:
                    guesses -= 1
                    print("##########################################################\n")
                    print(
                        "Oops! That is not a valid letter. You have no warnings left, so you lose one guess:",
                        get_guessed_word(secret_word, letters_guessed)
                    )
                    print("\n##########################################################")

                else:
                    vowels = ['a', 'e', 'i', 'o', 'u']
                    guesses -= 2 if i in vowels else 1
                    print("##########################################################\n")
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                    print("\n##########################################################")

        if guesses < 1: break

    total_score = guesses * len(set(secret_word))  # set() gives only unique letters of a string

    print(
        '\nSorry, you ran out of guesses. The word was "{}"'.format(secret_word) if guesses < 1
        else '\nCongratulations you won!!! The total score for this game is: ' + str(total_score)
    )


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """

    if len(my_word) != len(other_word):
        return False

    check_word = ''
    count_spaces = 0

    for letter in range(len(my_word)):
        if my_word[letter] == other_word[letter]:
            check_word += my_word[letter]

        elif my_word[letter] == '_':
            count_spaces += 1

    return (len(check_word) + count_spaces) == len(other_word)


# my_word = "he__o"
# other_word = "hello"
# a = match_with_gaps(my_word, other_word)
# print(a)


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """

    matched_words = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matched_words.append(word)

    if matched_words:
        print(' '.join(matched_words))

    else:
        print("There are no matches to your word")


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """

    guesses = 6  # User starts with 6 guesses & 3 warnings
    warnings = 3

    # Introduction of the game to the user
    print("\n---------------------------------------------")
    print('Welcome to the Hangman Game!!!')
    print("I'm thinking of a word that is {} letters long".format(len(secret_word)))
    print("---------------------------------------------")

    letters_guessed = []  # Stores all user inputs

    while not is_word_guessed(secret_word, letters_guessed):  # Keep looping until user guesses all letters in word

        print("\nSECRET WORD:", get_guessed_word(secret_word, letters_guessed))
        print("\nYou have {}".format(guesses), "guesses" if guesses > 1 else "guess", "left: ")
        print("You have {}".format(warnings), "warnings" if warnings > 1 else "warning", "left")
        print("Available letters: ", get_available_letters(letters_guessed))
        print("Letters already guessed: ", ' '.join(letters_guessed))

        user_letters = str.lower(input("Please guess a letter: "))  # User input: turns all letters into lowercase
        print()

        if "*" in user_letters and len(secret_word) > 4:  # Allow access to hints if secret word is > 4 letters
            print("##########################################################\n")
            print("Possible word matches are: \n")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            print("\n##########################################################")

        elif "*" in user_letters and len(secret_word) <= 4:  # Disallow access to hints if secret word is <= 4 letters
            print("##########################################################\n")
            print("Can't use HINT if the length of SECRET WORD is less than 4 !!!",
                  get_guessed_word(secret_word, letters_guessed))
            print("\n##########################################################")

        # If user inputs character that has already been guessed (not including "*" for HINT)
        elif user_letters in letters_guessed:
            if warnings >= 1:  # If there are 1 or more warnings left
                warnings -= 1
                print("##########################################################\n")
                print(
                    "OOPS! You\'ve already guessed that letter. You have", warnings, "warning" if warnings == 1
                    else "warnings", "left:", get_guessed_word(secret_word, letters_guessed)
                )
                print("\n##########################################################")
            else:  # If all 3 warnings are used, take off 1 guess
                guesses -= 1
                print("##########################################################\n")
                print("OOPS! You\'ve already guessed that letter. You have no warnings left, so you lose one guess:",
                      get_guessed_word(secret_word, letters_guessed)
                      )
                print("\n##########################################################")

        else:  # If user has NOT inputted a character more than once, do the following below

            letters_guessed.append(user_letters)

            for i in user_letters:  # Loops through user input
                if i in secret_word:  # If user guesses letter that IS IN secret word
                    print("##########################################################\n")
                    print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                    print("\n##########################################################")
                    break
                else:  # If user guess is not in secret word
                    # If user's guess IS NOT a letter & they have 1 OR MORE WARNINGS left:
                    if not str.isalpha(i) and warnings >= 1:
                        warnings -= 1  # Remove a warning
                        print("##########################################################\n")
                        print(
                            "OOPS! That is not a valid letter. You have", warnings, "warning" if warnings == 1
                            else "warnings", "left:", get_guessed_word(secret_word, letters_guessed)
                        )

                    # If user's guess IS NOT a letter & they have NO WARNINGS left:
                    elif not str.isalpha(i) and warnings < 1:
                        guesses -= 1  # Remove a guess
                        print("##########################################################\n")
                        print(
                            "OOPS! That is not a valid letter. You have no warnings left, so you lose one guess:",
                            get_guessed_word(secret_word, letters_guessed)
                        )

                    else:  # If user's guess is a WRONG LETTER
                        print("##########################################################\n")
                        vowels = ['a', 'e', 'i', 'o', 'u']
                        guesses -= 2 if i in vowels else 1  # User loses 2 guesses if wrong letter is vowel, else -1 guess
                        print("OOPS! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))

                    # Option to get a HINT (only if secret word < 4 letters) if user guesses letter wrong
                    print(
                        '\nHaving trouble?: Press "*" for a HINT only if your word is GREATER THAN 4 letters long !!!\n'
                        '>>> You', 'CAN' if len(secret_word) > 4 else 'CANNOT', 'use the HINT !!!')
                    print("\n##########################################################")

        if guesses < 1: break  # GAME ENDS: Exit loop if user runs out of guesses

    total_score = guesses * len(set(secret_word))  # set() gives only unique letters of a string
    max_score = 6 * len(set(secret_word))
    percent_total_score = (total_score / max_score) * 100

    print(
        '\nSorry, you ran out of guesses. The word was "{}"'.format(secret_word) if guesses < 1
        else '\nCongratulations you won!!! The total score for this game is: ' + str(total_score) +
             "/{max} ({percent_score}%)".format(max=max_score, percent_score=round(percent_total_score, 1))
    )


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = "banana"
    # # secret_word = choose_word(wordlist)
    # # hangman(secret_word)

    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    # secret_word = "apple"  # Test with word: apple
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

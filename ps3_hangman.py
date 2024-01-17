# Hangman game
#

# -----------------------------------


import random
import string
numofTurns = 8

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    with open(WORDLIST_FILENAME) as f:
        wordList = f.read().splitlines()

    print(len(wordList), "words loaded.")

    return wordList


def chooseWord(wordList):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """

    return random.choice(wordList)


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    wordGuessed = False
    for char in secretWord:
        if char in lettersGuessed:
            wordGuessed = True
        else:
            wordGuessed = False
            break
    return wordGuessed


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ''

    for char in secretWord:
        if char in lettersGuessed:
            guessedWord = guessedWord + char
        else:
            guessedWord = guessedWord + " _ "
    return guessedWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    allLetters = (string.ascii_lowercase)

    for char in lettersGuessed:
        if char in allLetters:
            allLetters = allLetters.replace(char, '')
    return allLetters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    lettersGuessed = ''
    mistakesMade = 0
    availableLetters = getAvailableLetters(lettersGuessed)
    guessesLeft = numofTurns
    guess = ''
    gameWon = False
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' +
          str(len(secretWord)) + ' letters long')

    while (mistakesMade < numofTurns):
        print('_ _ _ _ _ _ _ _\n')
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            gameWon = True
            break

        print('You have', str(guessesLeft), 'guesses left.')
        print('Available Letters:', str(availableLetters))
        guess = input('Please guess a letter: ')
        guess = guess.lower()
        lettersGuessed = lettersGuessed + guess
        guessedWord = getGuessedWord(secretWord, lettersGuessed)
        if guess not in availableLetters:
            print("Oops! You've already guessed that letter:", guessedWord)
        elif guess in secretWord:
            print('Good guess:', guessedWord)
            availableLetters = getAvailableLetters(lettersGuessed)
        elif guess in availableLetters:
            print('Oops! That letter is not in my word:', guessedWord)
            availableLetters = getAvailableLetters(lettersGuessed)
            mistakesMade += 1
            guessesLeft -= 1

    if not gameWon:
        print('_ _ _ _ _ _ _ _\n')
        print("Sorry, you ran out of guesses. The word was", secretWord + '.')


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordList = loadWords()
secretWord = chooseWord(wordList).lower()

hangman(secretWord)

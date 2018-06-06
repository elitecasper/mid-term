# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
#wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return all(letter in lettersGuessed for letter in secretWord)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    def find_characters(character, word):
        ''' function to get all differnt indexex for same letter in a string
        inputs: character, or the letter looked for
                word: string inside which we will look for letter's indexes
        '''
        found = []
        last_index = -1
        while True:
            try:
                last_index = word.index(character, last_index+1)
            except ValueError:
                break
            else:
                found.append(last_index)
        return found

    lettersRevealed = ['_ ']*len(secretWord)
    for letter in lettersGuessed:
        if letter in secretWord:
            indexes = find_characters(letter, secretWord)
            for indx in indexes:
                lettersRevealed[indx] = letter + ' '
                
    wordRevealed = ''        
    for i in lettersRevealed:
        wordRevealed += i
    return wordRevealed




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alph_letters = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        if letter in alph_letters:
            alph_letters.remove(letter)
    return ''.join(alph_letters)

    

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
    def charsNumber(word):
        '''
        input: word
        output: dictionary of caracters presented in word valued to
        the number of times they show up in word
        '''
        charDict = {}
        for i in word:
            if i in list(charDict.keys()):
                charDict[i] += 1
            else:
                charDict[i] = 1
        return charDict
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", str(len(secretWord)), " letters long.")
    charsDict = charsNumber(secretWord)
    lettersGuessed = []
    winLettersGuessed = []
    guessesCounter = 8
    winCounter = 0
    while (guessesCounter !=0 and winCounter != len(secretWord)):
        print("------------")
        print("You have", str(guessesCounter), "guesses left")
        print("Available Letters:", getAvailableLetters(lettersGuessed),end='')
        letterGiven = str(input("Please guess a letter:"))
        if letterGiven in list(charsDict.keys()):
            if letterGiven in lettersGuessed:
                print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, winLettersGuessed))
                next
            else:
                winLettersGuessed += letterGiven
                winCounter += charsDict[letterGiven]
                print("Good guess:", getGuessedWord(secretWord, winLettersGuessed))
        else:
            if letterGiven in lettersGuessed:
                print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, winLettersGuessed))
                next
            else:
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord, winLettersGuessed))
                guessesCounter -= 1
        if guessesCounter == 0:
            print("------------")
            print("Sorry, you ran out of guesses. The word was", secretWord+".")	
        lettersGuessed += letterGiven
        if winCounter == len(secretWord):
            print("------------")
            print("Congratulations, you won!")
            break

hangman(chooseWord(loadWords()))






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)

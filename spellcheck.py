# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])

    selection = getSelection()
    word = spellCheck()

    loop = True
    while loop:
        if selection == '1':
            linearSearch(dictionary, word)
        elif selection == '2':
            binarySearch(dictionary, word)
        elif selection == '3':
            linearSearch(aliceWords)    
        elif selection == '4':
            binarySearch(aliceWords)
        elif selection == '5':
            loop = False
# end main()

def getSelection():
    print('\nMain Menu')
    print('1: Spell Check a Word (Linear Search)')
    print('2: Spell Check a Word (Binary Search)')
    print('3: Spell Check Alice In Wonderland (Linear Search)')
    print('4: Spell Check Alice In Wonderland (Binary Search)')
    print('5: Exit')

    return input('Enter menu selection (1-5): ')
# end of getSelection()

def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()

# Get desired word
def spellCheck():
    return input('Please enter a word: ')

# Linear Searches
# def linearSearch(array, item):
    
# end of linearSearch()

# Binary Searches
def binarySearch(array, item):
    ui = len(array) - 1
    li = 0

    i = 0
    while i < len(array):
        mi = int(((ui + li) / 2))
        if item == array[mi]:
            return mi
        elif item < array[mi]:
            ui = mi - 1
        elif item > array[mi]:
            li = mi + 1
        i += 1
    return -1
# end of binarySearch()

# Call main() to begin program
main()

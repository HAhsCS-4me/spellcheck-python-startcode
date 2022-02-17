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

    loop = True
    while loop:
        selection, word = getSelection()
        if selection == '1':
            option1 = linearSearch(dictionary, word)
            output(option1, word)
        elif selection == '2':
            option2 = binarySearch(dictionary, word)
            output(option2, word)
        elif selection == '3':
            option3 = linearSearch(aliceWords)
            output(option3, word)    
        elif selection == '4':
            option4 = binarySearch(aliceWords)
            output(option4, word)
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

    selection = input('Enter menu selection (1-5): ')
    word = input('Please enter a word: ')
    
    return selection, word.lower()
# end of getSelection()

def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()

# Linear Searches
def linearSearch(anArray, item):
    for i in range(len(anArray)):
        if anArray[i] == item:
            return i
    return -1 
#end of linearSearch()

# Binary Searches
def binarySearch(anArray, item):
    ui = len(anArray) - 1
    li = 0

    while ui >= li:
        mi = (ui + li) // 2
        if item == anArray[mi]:
            return mi
        elif item < anArray[mi]:
            ui = mi - 1
        else:
            li = mi + 1
    return -1
# end of binarySearch()

# Output
def output(option, word):
    if option >= 0:
        print(f'{word} is IN the dictionary position {option}')
    else:
        print(f'{word} is NOT IN the dictionary')

# Call main() to begin program
main()

# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])

    loop = True
    while loop:
        selection = getSelection()
        if selection == '1':
            word = input('Please enter a word: ')
            # Starting time
            startTime = time.perf_counter()
            option1 = linearSearch(dictionary, word.lower())
            # Ending time
            endTime = time.perf_counter()
            # Time elapsed
            timeElapse = endTime - startTime
            sel1And2(option1, word, timeElapse)
        elif selection == '2':
            word = input('Please enter a word: ')
            # Starting time
            startTime = time.perf_counter()
            option2 = binarySearch(dictionary, word.lower())
            # Ending time
            endTime = time.perf_counter()
            # Time elapsed
            timeElapse = endTime - startTime
            sel1And2(option2, word)
        # Womk
        elif selection == '3':
            nonwords = 0  
            # Starting time
            startTime = time.perf_counter()
            for i in range(len(aliceWords)):
                option3 = linearSearch(dictionary, aliceWords[i].lower())
                if option3 < 0:
                    nonwords += 1
            # Ending time
            endTime = time.perf_counter()
            # Time elapsed
            timeElapse = endTime - startTime
            print(f'Number of words not found in dictionary: {nonwords} ({timeElapse} seconds).')
        elif selection == '4':
            nonwords = 0 
            # Starting time
            startTime = time.perf_counter()      
            for i in range(len(aliceWords)):
                option3 = binarySearch(dictionary, aliceWords[i].lower())
                if option3 < 0:
                    nonwords += 1
            # Ending time
            endTime = time.perf_counter()
            # Time elapsed
            timeElapse = endTime - startTime
            print(f'Number of words not found in dictionary: {nonwords} ({timeElapse} seconds).')
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
    return selection
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
# end of linearSearch()

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

# Output for selections 1 and 2
def sel1And2(option, word, time):
    if option >= 0:
        print(f'{word} is IN the dictionary position {option} ({time} seconds).')
    else:
        print(f'{word} is NOT IN the dictionary ({time} seconds)')
# end of selOneAndTwo()

# Call main() to begin program
main()
import timeit

nums = [3, 5, 7, 8, 1, 3, 6, 12, 34, 76, 23, 4, 43]
faveNum = input('choose a number: ')

def linearSearch(anArray, item):
    for i in range(len(anArray)):
        if anArray[i] == item:
            return i
    return -1

print(linearSearch(nums, faveNum))
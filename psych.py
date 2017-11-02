# Functions for Statistics in Psychological Research
import math
import numpy
from collections import Counter
# calculates the median of a given list
def median(numbers):
    numbers.sort()
    length = len(numbers)
    if (length % 2 == 0):
        # for lists with an even length
        return (numbers[int(length / 2) - 1] + numbers[int(length / 2)]) / 2
    else:
        # for lists with an odd length
        return numbers[int((length + 1) / 2) - 1]
    
# calculates the mean of a given list
def mean(numbers):
    addition = 0
    for x in numbers:
        addition = addition + x
    return addition / len(numbers)

# calculates the range of a given list
def myrange(numbers):
    numbers.sort()
    minimum = numbers[0]
    maximum = numbers[-1]
    return maximum - minimum


# calculates the sum of squares
def sumsquares(numbers):
    addition = 0
    squaredadd = 0
    for x in numbers:
        addition = addition + x
        squaredadd = squaredadd + (x * x)
    return squaredadd - ((addition * addition) / len(numbers))


# calculates variance
def variance(numbers):
    return sumsquares(numbers) / (len(numbers) - 1)

# calculates standard deviation
def standdev(numbers):
    return math.sqrt(variance(numbers))

# given a list of numbers and a countby, return a frequency distribution
# in form of (lower bound, upper bound, count)
def freqdist(numbers, countby):
    if (min(numbers) % countby == 0):
        lowest = min(numbers)
    else:
        lowest = min(numbers)
        while (lowest % countby != 0):
            lowest -= 1
    binlist = []
    while (lowest < max(numbers)):
        binlist.insert(0, lowest)
        lowest += countby
    bincounts = []
    for eachbin in binlist:
        bincount = 0
        for num in numbers:
            if (num >= eachbin) and (num < eachbin + countby):
                bincount += 1
        bincounts.insert(0, (str(eachbin) + '-' + str(eachbin + countby - 1), bincount))
    return bincounts


#returns the relative grouped frequency distribution
def rfdist(numbers, countby):
    fdist = freqdist(numbers, countby)
    length = len(numbers)
    return [(bounds, result / length) for (bounds, result) in fdist]

# returns an array of (number, zscore) pairs for numbers in a list
def zscores(numbers):
    m = mean(numbers)
    sd = standdev(numbers)
    return [(number, (number - m) / sd) for number in numbers]


                         

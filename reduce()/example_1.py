"""
The reduce() function, available in Python's functools module, is used to apply a rolling computation to pairs of elements in an iterable (e.g., a list).
It's useful when you want to accumulate or reduce a list of values down to a single result using a specified binary function (a function that takes two inputs).

Syntax :
    reduce(function, iterable, initializer=None)

1. function: A function of two arguments that reduce() applies cumulatively to the items in the iterable.
2. iterable: The sequence of elements you want to reduce.
3. initializer (optional): A starting value for the accumulation. If provided, this becomes the first value to be
   accumulated with the first element of the iterable.
"""

# Summing a List of Numbers

from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_total = reduce(lambda x, y: x+y, numbers)
print("Total Sum : ", sum_total)

def summing_function(x, y):
    return x+y

summation = reduce(summing_function, numbers)
print(summation)

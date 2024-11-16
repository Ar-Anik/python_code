from functools import reduce

numbers = [5, 3, 8, 2, 7]
max_value = reduce(lambda x, y: x if x >= y else y, numbers)

print("Maximum Value : ", max_value)

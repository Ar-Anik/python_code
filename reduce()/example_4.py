from functools import reduce

words = ["Hello", "World", "From", "Reduce", "Function"]
sentence = reduce(lambda x, y: x + " " + y, words)

print(sentence)

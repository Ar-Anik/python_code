"""
We can inspect some attributes of the lambda function to see more details like its name (which is <lambda>), its code object, and the variables it uses.
"""

x = lambda a, b: a + b + 10

print(x.__name__)

print(x.__code__)

print(x.__code__.co_code)
print(x.__code__.co_consts)
print(x.__code__.co_varnames)
print(x.__code__.__dir__())
print(x.__hash__())
print(x.__dir__())
print(x.__sizeof__())
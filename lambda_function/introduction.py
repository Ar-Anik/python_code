"""
A lambda function is an anonymous function defined using the lambda keyword. Unlike normal functions created using the def keyword, lambda functions are typically
used for short, simple operations and are often used in functional programming contexts like within map(), filter(), or reduce().

Syntax:
    lambda arguments: expression
"""

square = lambda x: x ** 2
print(square(5))

print(square)

"""
The above lambda function work like :

def func(x):
    return x ** 2

square = func
print(square(5))

"""

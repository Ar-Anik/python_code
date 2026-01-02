"""
Python's NamedTuple is a powerful tool that combines the memory efficiency of a regular tuple with the readability of
an object. It allows for accessing data using dot notation (e.g., car.color) instead of just indexes (e.g., car[1]).

There are two ways to implement them: the classic collections.namedtuple and the modern type-hinted typing.NamedTuple.
"""

"""
Basic: The Factory Function
This is the classic way to create a NamedTuple. It is great for quick data grouping without needing complex classes.
"""
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

print("Class Type : ", Point)

p = Point(10, 20)

print("p type : ", type(p))

# It even inherits from 'tuple'
print(isinstance(p, tuple))

print(f'X coordinate : {p.x}')
print(f'Y coordinate : {p[1]}')

x_val, y_val = p
print(f'Unpacked : {x_val}, {y_val}')

"""
Think of namedtuple as a factory function. Instead of building an object directly, it builds a new class (a subclass of 
the built-in tuple) and returns that class.

When we run Point = namedtuple('Point', ['x', 'y']), Python dynamically creates a class that looks and behaves like this:
"""

class Point(tuple):
    def __new__(cls, x, y):
        return super().__new__(cls, (x, y))

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    # Plus some extra helper methods like __repr__ and _asdict

"""
Q : Why is it done this way?
-> By creating a class definition first, Python ensures that every instance we create (like p1, p2, p3) shares the same 
structure. This makes it:
1. Memory Efficient: Since it's a class based on tuple, it doesn't need a __dict__ for every instance.
2. Reusable: We can use Point to create thousands of coordinates, and they will all have the .x and .y properties available.
"""

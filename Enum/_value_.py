"""
In Python, enum members are objects of the enum class. Every enum member has an internal attribute called _value_, which
stores the actual value we assigned.
"""

from enum import Enum

class Color(Enum):
    RED = 1

print(Color.RED._value_)
print(Color.RED.value)

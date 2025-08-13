"""
Enum in Python (from enum import Enum) is used when we want to define a set of named constant values that are
logically related and shouldn’t change during program execution.
"""

from enum import Enum

class Status(Enum):
    ACTIVE = 1
    INACTIVE = 2

status = 1
if status == Status.ACTIVE.value:
    print("Active")

"""
Python does this behind the scenes:
    1. Creates a class Status that inherits from Enum.
    2. Stores members (ACTIVE, INACTIVE) in a mapping inside the class:
        Status.__members__ → an OrderedDict of names and enum members.
    3. Each member is an instance of the Status class, not just an int or string.
"""

print(Status.__members__)

print(Status.ACTIVE.name)
print(Status.ACTIVE.value)
print(Status.ACTIVE)   # Here, Status → the Enum class name. ACTIVE → the name of the member. Together → "this is the ACTIVE member of the Status enum"

class Value(Enum):
    A = 1
    B = 2
    C = 3

    def __str__(self):
        return str(self.value)

print(Value.A)
print(Value.B)
print(Value.C)

"""
-> When to use Enum:
    * When values are fixed and known ahead of time (days of week, user roles, HTTP methods, states in a workflow, etc.).
    * When you want meaningful names instead of raw numbers or strings.
    * When you want type safety and to prevent invalid values.
"""

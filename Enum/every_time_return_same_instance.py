"""
Each Enum member is a single, unique instance of the Enum class (or its subclass). That means:
- When we access MyEnum.MEMBER multiple times, we always get the same object (same instance).
- Enum members are not plain ints or strings (even if we assign them int/string values). They are instances of the Enum subclass.
- The value we assign (1, "abc", etc.) is stored in the .value attribute, but the member itself is an object.
"""

from enum import Enum

class Status(Enum):
    ACTIVE = 1
    INACTIVE = 2

obj_1 = Status.ACTIVE
obj_2 = Status.ACTIVE

obj_3 = Status.INACTIVE
obj_4 = Status.INACTIVE

print(type(obj_1))
print("Is Object_1 Instance of Status : ", isinstance(obj_1, Status))
print("object_1 is object_2 : ", obj_1 is obj_2)

print(type(obj_3))
print("Is Object_3 Instance of Status : ", isinstance(obj_3, Status))
print("object_3 is object_4 : ", obj_3 is obj_4)

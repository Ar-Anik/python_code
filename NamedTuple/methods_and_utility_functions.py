"""
Since typing.NamedTuple uses class syntax, we can actually add methods to it. we can also use built-in helper methods like _asdict() and _replace().
"""

from typing import NamedTuple

class Rectangle(NamedTuple):
    width: float
    height: float

    def area(self):
        return self.width * self.height

    def scale(self, factor: float):
        # Since it's immutable, we return a NEW instance
        return self._replace(width=self.width * factor, height=self.height * factor)


rect = Rectangle(10, 5)
print(f'Area : {rect.area()}')

# Using _replace to create a new version with one value changed
big_rect = rect.scale(2)
print(big_rect)
print("New Area : ", big_rect.area())

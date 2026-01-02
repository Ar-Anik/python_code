"""
Using typing.NamedTuple is the modern standard. It makes the code much cleaner, supports IDE autocomplete better and allows
for type hints.
"""

from typing import NamedTuple

class User(NamedTuple):
    id: int
    username: str
    email: str
    is_active: bool=True        # we can also set default values here

new_user = User(1, 'anik', 'anik@gmail.com')

print(new_user)
print(new_user.username)
print(new_user.is_active)

"""
Note: Just like regular tuples, NamedTuple is immutable. We cannot change new_user.username = "rob" after it is created.
"""

# new_user.username = 'Rob'

# Convert to a dictionary using ._asdict()
user_dict = new_user._asdict()

print('Type : ', type(user_dict))
print('Dictionary : ', user_dict)
print('Accessing Email : ', user_dict['email'])


raw_data = {
    'id': 2,
    'username': 'sourov',
    'email': 'sourov@gmail.com'
}
another_user = User(**raw_data)
print('Another User : ', another_user)


"""
1. The "Metaclass" Magic
When Python sees class User(NamedTuple):, it doesn't create a standard mutable object. Instead the NamedTuple parent class 
uses a "metaclass" to intercept the class creation.

It looks at the variables we defined inside the class and essentially does the following:
    - It collects the names (id, username, etc.).
    - It collects the types (int, str, etc.) from the annotations.
    - It builds a new tuple-based class where each field is mapped(by create property) to an index (0, 1, 2, 3).


2. How the Fields are Created
Unlike a normal class where fields are stored in a dictionary (__dict__), NamedTuple fields are stored in a specific 
order, just like a list or a regular tuple.
    - id becomes index 0.
    - username becomes index 1.
    - email becomes index 2.
    - is_active becomes index 3.

Python automatically generates property getters for this. When we call user.username, Python is actually executing 
something similar to return self[1].


3. Handling Default Values
In this example, is_active: bool = True has a default value.

Standard collections.namedtuple makes it very hard to set defaults. typing.NamedTuple handles this by storing the 
default values in a special hidden attribute called _field_defaults.

When we create an instance without providing is_active, Python checks this hidden dictionary and fills it in for this.


# If we were to "peek" at what Python generates for your User class, it would look roughly like this:
"""

class User(tuple):
    # Python automatically generates the constructor
    def __new__(cls, id, username, email, is_active=True):
        return super().__new__(cls, (id, username, email, is_active))

    # Python generates these properties for dot notation
    @property
    def id(self):
        return self[0]

    @property
    def username(self):
        return self[1]

    # ... and so on


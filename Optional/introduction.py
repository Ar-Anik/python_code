"""
Optional from typing is use code because some attributes might not always have a value (they can be None).

Optional[str] = str | None  # (Python 3.10+ syntax)
"""

from typing import Optional

def greet(name: Optional[str]):
    if name is None:
        print("Hello Stranger")
    else:
        print(f"Hello {name}")

greet("Anik")
greet(1)    # because Python’s type hints are not enforced at runtime.

greet(None)
# greet()

def congo(name: Optional[str] = None):
    if name is None:
        print("Hello Stranger")
    else:
        print(f"Hello {name}")

congo()

"""
> With and Without Optional, both versions behave identically because Python doesn’t enforce type hints by default.
> The only difference is that Optional[str] is metadata for us, our team, and our tools (not the Python interpreter).
"""

"""
1. Assertions Can Be Disabled : If Python is run with the -O (optimize) flag, all assertions are ignored, and the code after assert is not executed.
Command :  python -O script.py

2. Use Assertions for Development Only : Assertions are typically used for internal consistency checks during development, not as a substitute for proper error handling in production code.
"""

"""
# Advantages of assert
1. Helps catch bugs early by verifying assumptions.
2. Provides meaningful debugging messages when used with error messages.
3. Easy to write and read.
"""

"""
# Disadvantages
1. Can be disabled, so they should not be relied upon for essential error handling.
2. Not suitable for handling runtime errors in production systems.
"""

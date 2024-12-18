"""
The exec() function in Python is a built-in function used to execute dynamically created Python code, which can be provided as a string or object code.

Syntax: exec(object, globals=None, locals=None)

Here :
    1. object: A string or code object that contains valid Python code to execute.
    2. globals (optional): A dictionary to define the global namespace where the code is executed.
    3. locals (optional): A dictionary to define the local namespace where the code is executed.
"""

"""
Key Points:
    1. Dynamically executes Python code at runtime.
    2. You can execute any Python statement such as assignments, loops, or function definitions.
    3. Not for expressions alone; for expressions, you use eval() instead.
    4. Be cautious when using exec() with untrusted input, as it can execute malicious code.
"""

# Example

code = "x = 5\ny = 10\nprint('Sum: ', x+y)"
exec(code)

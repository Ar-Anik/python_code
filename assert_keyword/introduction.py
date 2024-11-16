"""
The assert keyword in Python is a debugging aid used to test whether a condition is true. If the condition evaluates to True, the program continues execution.
If the condition evaluates to False, an AssertionError is raised, optionally with an error message.

## Syntax :
    assert condition, message
here,
    condition :  The expression to evaluate. If False, an AssertionError is raised.
    message(optional) : A custom error message that provides more context about the failed assertion.
"""

# Basic Validation
x = -1
assert x > 0, "x must be positive"

# If raise AssertionError, the code after assert is not executed.

# Testing
def add(a, b):
    print("Addition execute.")
    return a + b

assert add(2, 3) == 5, "Addition function not give expected value."


"""
Q : What is AssertionError?
---> An AssertionError is an exception in Python that is raised when an assert statement fails. It indicates that a condition the program expected to be true 
is actually false, and the program cannot continue executing in a consistent state.

Q : What happen when AssertionError Raise?
---> When raised:
        1. Python stops executing the program.
        2. Displays a traceback to show where the error occurred.
        3. If an optional message is provided, it is included in the error output.
"""

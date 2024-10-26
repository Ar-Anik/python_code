"""
`lambda` functions work similarly to normal functions but with a few key differences:
1. Anonymous Nature: Lambda functions don’t have a name; they are expressions rather than statements.
2. Single Expression: Lambda functions can only contain a single expression, which is immediately evaluated and returned. There are no statements (e.g., print, return) allowed inside a lambda.
3. Function Object Creation: When a lambda function is defined, it creates a function object, just like a normal def function. The function is executed when called, and the result is returned.
4. No Function Name Binding: Lambda functions are typically not bound to a name unless explicitly assigned to a variable. The function object is created dynamically and can be discarded after use.

Internally, Python generates a code object when a lambda function is defined, which is the same process used for normal functions.
`The main difference is that it doesn’t generate a name for the function (unless we assign one).`
"""

"""
When we create a lambda function like x = lambda a: a + 10 and print x, it will show us the object reference, not the actual code inside the function. If we want to see the 
actual code or "real face" of the lambda function, we can use the `dis` module to disassemble the bytecode or inspect its attributes.
"""

from dis import dis

x = lambda a: a + 10
# print(x)       # it show object reference like <function <lambda> at 0x7fab77b83040>
dis(x)

"""
# output :
 19           0 LOAD_FAST                0 (a)
              2 LOAD_CONST               1 (10)
              4 BINARY_ADD
              6 RETURN_VALUE

Above shows the internal steps taken by the lambda function : 
    1. It loads the variable a.
    2. It loads the constant 10.
    3. It adds them together.
    4. It returns the result.
"""
exec("""
def greet(name):
    print(f"Hello, {name}")
""")

greet("Anik")

"""
Difference Between exec() and eval(): 
1. exec() can execute statements (like loops, function definitions, assignments, etc.).
2. eval() can only evaluate expressions (like 1 + 2, a * b, etc.).
"""

# Detecting Errors Early
def divide(a, b):
    assert b != 0, "Division by zero is not allowed"
    return a/b

print(divide(4, 2))
print(divide(99, 2))
print(divide(10, 0))

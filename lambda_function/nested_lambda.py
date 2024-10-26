nested_lambda = lambda x: lambda y: x/y
divider = nested_lambda(100)
print("Result : ", divider(5))

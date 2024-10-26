# map function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print("Square Number : ", squared_numbers)

# filter function
even_numbers = list(filter(lambda x: x%2==0, numbers))
print("Even Numbers : ", even_numbers)

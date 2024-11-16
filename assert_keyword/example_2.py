def calculate_area(length, width):
    assert length > 0 and width > 0, "Length and Width must be positive"
    return length * width

area = calculate_area(5, 10)
print(area)

area = calculate_area(-5, 10)
print(area)

"""
if run this script with, `python -O example_2.py` then assert will be ignore.
"""


def calc_rectangle(width, length):
    """the function calculates the area of a rectangle"""
    area = length * width
    print(f"The area of your rectangle is: {area}")

width = float(input(f"What is the width?: "))
length = float(input(f"Length?: "))
calc_rectangle(width, length)


import turtle


"""PUT YOUR FUNCTIONS HERE"""

# Create a turtle object
# t = turtle.Turtle()
#
# Hide the turtle and set speed
# t.speed(1)  # 1 is slow, 10 is fast, 0 is instant
# t.hideturtle()

# Create a window to draw in
# Create a new turtle screen and set its background color
# screen = turtle.Screen()
# screen.bgcolor("darkblue")
# Set the width and height of the screen
# screen.setup(width=600, height=600)
# Clear the screen
# t.clear()

# def draw_square(t, length):
#     """Draws a square with the given side length."""
#     for _ in range(4):
#         t.forward(length)
#         t.left(90)

"""PUT YOUR DRAW CALLS TO FUNCTIONS HERE"""
# t.forward(length)
# t.left(90)






# draw_square(t,70)

# Close the turtle graphics window when clicked
# turtle.exitonclick()



# def square(length):
#     for i in range(4):
#         forward(length)
#         left(90)

# square(50)

# def collatz(x):
#     if x % 2 == 0:
#         return x // 2
#     else:
#         return x * 3 + 1

# print(collatz(3))
#
# a = 25 // 10
# b = 25 % 10
# print(a, b)
#
# x = 5
# print(x > 5)
# print(x <= 5)

# def is_close(x, y):
#     return abs(x - y) < 0.2
# print(is_close(1.5, 1.6))

def astronomy(n):
    if n > 0:
        print('stars')
        astronomy(n-1)
    else:
        print('moons')

astronomy(5)


def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

countdown(5)

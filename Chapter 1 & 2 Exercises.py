    #  Chapter 1 Exercise #

        # 1.9.2 #

print(round(42.5))
print(round(43.5))

# Python does neither consistently—instead, it rounds to
# the nearest even number. This behavior is known as round
# half to even or banker's rounding.

# When a number sits exactly
# halfway between two integers (ending in .5), Python checks the
# neighboring whole numbers and picks the one that is even:

# round(2.5) returns 2 (rounds down because 2 is even).
# round(3.5) returns 4 (rounds up because 4 is even).
# round(4.5) returns 4 (rounds down because 4 is even).
# round(5.5) returns 6 (rounds up because 6 is even).

# Negative numbers follow the exact same rule:round(-2.5) returns -2.

# round(-3.5) returns -4.

# Why Python does this:
# Grade-school arithmetic
# teaches "round half up" (where .5 always rounds up to the next number).
# However, in statistics, science, and finance, always rounding .5 upward
# introduces a cumulative upward bias. If you round thousands of numbers
# ending in .5 upward, the sum of those rounded values drifts higher than
# the true total.  By rounding to the nearest even number, roughly half of
# your .5 values round up and the other half round down, keeping the errors
# balanced and minimizing bias. This follows the IEEE 754 standard for
# floating-point arithmetic used across modern computing.  How to force
# traditional "round half up"If an assignment specifically requires
# standard school rounding, Python’s built-in round() cannot do it directly.
# You can use the standard library's decimal module instead:

#from decimal import Decimal, ROUND_HALF_UP

# Quantize to 0 decimal places using standard half-up logic
#value = Decimal('2.5').quantize(Decimal('1'), rounding=ROUND_HALF_UP)
#print(value)  # Outputs 3


        # 1.9.3 #

print(2++2)
# The answer is 4 #

#print(4 2)
# SyntaxError: invalid syntax. Perhaps you forgot a comma? #

#round(42.5
#vSyntaxError: '(' was never closed #


        # 1.9.4 #

# Guesses? #

#int
#float
#string
#function    # Type was int. It is giving type of argument, argument for f(x)'s. #
#function    # It makes sense this was float, after ^^^ this answer. #
#module      # Type is function. I see it now. #
#type
#class       # Type of what? lol

print(type(765))
print(type(2.718))
print(type('2 pi'))
print(type(abs(-7)))
print(type(abs(-7.0)))
print(type(abs))
print(type(int))
print(type(type))


        # 1.9.5 #

# How many seconds are there in 42 minutes 42 seconds?
print(f"There are {(42*60)+42} seconds in 42 minutes and 42 seconds.")
# How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
print(f"There are {1.609*10} miles in 10 kilometers.")
# If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?
print(f"My average pace in seconds per mile is {2562/16.09}")
# What is your average pace in minutes and seconds per mile?
print(f"My average pace in min and sec per mile is {(int((2562/16.09))//60)} minutes and {int((2562/16.09))-(int((2562/16.09))//60)*60} seconds.")
# What is your average speed in miles per hour?
print(f"My average in mph is {round((42.7/60),3)}")



    # Chapter 2 Exercise #

        # 2.11.2 #

# 17 = n
# SyntaxError: cannot assign to literal here.
# Maybe you meant '==' instead of '='?

x=y=1
# ^^^ this statement is just fine,
# but when I try to print, it has a problem
# print(x=y=1)
# SyntaxError: invalid syntax

n = 3+4.
print(n)
# the period didn't error for this statement

# name = "noodlez".
# ^^^ the period messed me up here, though

name = "noodlez";  # I keep forgetting to add quotes for these
# it doesn't stop my code, but it does tell me a thing. look below.
# (yellow triangle) Trailing semicolon in the statement : 117

# import maath
# ModuleNotFoundError: No module named 'maath'


    # 2.11.3

import math

# Part 1 #

radius = 5  # radius units in centimeters
volume = (4/3)*math.pi * radius**3  # volume in cubic centimeters
print(volume)

# Part 2 #

x = 42
print(math.cos(x)**2 + math.sin(x)**2)

# Part 3 #

print(f"e squared via ** = {math.e**2}")
print(f"e squared via math.pow = {math.pow(math.e, 2)}")
print(f"e squared via math.exp = {math.exp(2)}")
# The difference here is that the math.exp went to 2 less digits than the other 2
print(f"e to power of e = {math.exp(math.e)}")
print("")  # I assume I will learn how to seperate these lines without using an "empty" print function
print("Thank you very much for your time. Your Best Friend Noodlez")
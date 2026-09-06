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


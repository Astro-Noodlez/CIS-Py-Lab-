# Lab 2 CIS-12

# Part 1

name = "Noodlez"
age = 37  # Until tomorrow 9-1, in case I turn it in a bit later!
height = 6
favorite_color = "Red"

print(name)
print(age)
print(height)
print(favorite_color)

print(name, age, height, favorite_color)

print(f"Hey everyone,: My name is {name}, "
f"I am {height} ft tall and I am {age} "
f"years old. My favorite color is {favorite_color}.")

# Weird, all I did above was hit enter to break up the lines
# and it added the extra f string commands

print(f"What if I added my: age, {age} and my height, {height} together "
      f"and made it a floater?")

z = age + height
print(f"{z:.3f}")
print(f"I want to turn z into an integer that"
      f" looks like this: {z:d}")
print(f"So: z = {int(z)}")

print("Noodlez's car")     # I don't know if my name is like the word sheep
print('Noodlez\'s car')    # Do I make it plural-er or not! lol

dog_name = "Ripley"
dog_age = 2

print(f"""This is me, {name}, as a {age} year old man,
      typing a multi line string to tell you:
          that my dog, {dog_name}, is {dog_age} years old!""")

import math

r = 5
circle_area = math.pi * math.pow(r, 2)
print(round(circle_area, 1))

# Part 2

print(f"Here is the square root of my age: {math.sqrt(age):.4f}")

print(f" Here is the sin of my height: {math.sin(height):.4f}")

print(f"  Finally, Here is the cos of my height: {math.cos(height):.4f}")
print("   I also rounded everything to the 4th decimal place")


# Part 3

#The sum of age and 5.
print(f"My age in addition to 5 is: {age + 5}")   #I've worded the sentence in this way just to be different
#The difference between height and 4.
print(f"Four away from my height is: {height -4}")   #This line, too, is for ^^^^^ reason
#The product of age and height.
print(f"My age multiplied by my height is: {age * height}")   #Is it a "thing" to be self-conscious about coding?
#The quotient of height and 2.
print(f"My height divided by 2 is: {height/2}")
#The remainder of age divided by 3.
print(f"What's left after I divide my age by 3? It's {age % 3}")
#age raised to the power of 2.
print(f"My age squared: {age**2}")  #alternatively; math.pow(age, 2)


# Part 4
fahrenheit = int(input(f"What is the temperature in degrees fahrenheit(°F)?: "))
celsius = (fahrenheit - 32) * (5/9)
print(f"The answer is {celsius:.2f} degrees celsius(°C)!")


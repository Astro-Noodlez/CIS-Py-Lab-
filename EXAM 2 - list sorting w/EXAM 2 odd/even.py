# Prompt the user to enter a number as an integer
# It should pass the integer as an argument to your function
# Your program should print the result like so:
# If the number is Even state: "The number X is even"
# If the number is Odd state: "The number X is odd"
# X is the number input by the user.


def is_even(n):
    if n % 2 == 0:
        return 'The number is even'
    else:
        return 'The number is odd'



user_input = int(input("Enter a number: "))
choice = is_even(user_input)
print(choice)
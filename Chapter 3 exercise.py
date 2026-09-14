   # 3.11.1 #

# 1. Ask your favorite VA to “Write a function called repeat that takes a string and an
# integer and prints the string the given number of times.”

def repeat(text, times):
  for _ in range(times):
    print(text)

repeat("Nudz", 5)

# 2. If the result uses a for loop, you could ask, “Can you do it without a for loop?”

def repeat(text, times):
  print(*([text] * times), sep="\n")

repeat("Noodlez", 5)

# 3. Pick any other function in this chapter and ask a VA to write it. The challenge is to
# describe the function precisely enough to get what you want. Use the vocabulary you have
# learned so far in this book.

def print_lyrics():
  print("So here I am it's in my hands")
  print("And I'll savor every moment of this")      # I just triple quoted to block it off #
  print("So here I am alive at last")
  print("And I'll savor every moment of THIS")

print_lyrics()

    # 3.11.2 #

def print_right(text, text2, text3, text4):
    print(input('what is your name funny one?: '))
    print(end=' '*37)
    print(text, sep='\n')                              # I couldn't really figure it out
    print(end=" "*37)                                  # so i made this specifically for this one phrase
    print(text2, sep='\n')                             # I looked at yours after...it's amazing lol
    print(end=" "*35)
    print(text3, sep="\n")
    print(end=" "*37)
    print(text4, sep='\n')


print_right('how', 'now', 'brown', 'cow')

    # 3.11.3 #
# Write a function called triangle that takes a string and an integer and draws a pyramid
# with the given height, made up using copies of the string. Here’s an example of a pyramid
# with 5 levels, using the string 'L'.

def triangle(text, n):
    for _ in range(n):
        print(text*(_+1))

triangle("N", 10)


    # 3.11.4 #

def rectangle(letter, x, y):
    for a in range(x):
        for b in range(y):
            print(letter, end='')
        print()

R = rectangle

R("N", 2,7)
R("o", 3,8)
R("d", 2,9)
R("l", 2,10)
R("e",2,11)
R("z",2,12)


    # 3.11.5 #

# def bottle_verse(n):
#     for n in range(99, 0, -1):                             # this was my try
#         bottle_verse(n)
#         print(f'{n} bottles of pop on the wall')
#
# bottle_verse(99)

def bottle_verse(n):
    if n <= 0: return                                                  # I had to look at yours on this one
    print(f"""{n} bottle{'' if n == 1 else 's'} of pop on the wall
{n} bottle{'' if n == 1 else 's'} of pop
Take one down, pass it around
{n-1} bottle{'' if n-1 == 1 else 's'} of pop on the wall
    """)

def bottle_song(n):
    for verse in range(n, -1, -1):
        bottle_verse(verse)

bottle_song(5)

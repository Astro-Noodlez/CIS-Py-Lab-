"Problem 1"

import math

r = 5
a = math.pi * 5**2

v = (4/3) * math.pi * r**3

a_side = 3
b_side = 4
c_sq = a_side**2 + b_side**2
pyt = math.sqrt(c_sq)

"my version"
c = math.sqrt(a_side**2+b_side**2)
"end of my version"



"Problem 2"


first_name = "Noodlez"
last_name = "Essex"
full_name = first_name + ' ' + last_name
name_len = len(full_name)

print(a, v, pyt, int(c), name_len, full_name, full_name.upper(), full_name.lower())

"Problem 3"

age = 37
weight = 242
height = 72.0
print((type(age), type(weight), type(height)))
bmi = (weight/height**2) * 703
print(bmi)


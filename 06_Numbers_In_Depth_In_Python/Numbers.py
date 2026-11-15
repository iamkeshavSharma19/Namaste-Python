x = 2
y = 3
z = 4
print((x + y) * z)
print(40 + 2.23)
# print("Keshav" + 3) #!TypeError: can only concatenate str (not "int") to str.
print(int(2.23)) # 2
print(float(40)) # 40.0

# ? Operator Overloading.
print("Keshav" + " " + "Sharma")
print(y % 2) # 1
# ? Calculating the Powers.
print(z ** 2) # 16
print(100 ** 2) # 10000
# ~ Almost Every other language fails at calculating 2 to the Power 100,but python does'not fails,it gives the exact answer, no matter how big the calculation or computation is.
print(2 ** 100) # 1267650600228229401496703205376
# todo === Study About repr, str and print and differences between them
print(repr("Python"))
print(str("Python"))
print("Python")
print(1  < 2)
print(5.0 == 5.0)
# ? Below 2 statements are exactly same.
print(x  < y  < z) #True
print(x  < y and y  < z) #True

# & Below 2 statements Are also exactly same.
print(1 == 2  < 3) #False
print(1 == 2 and 2  < 3) #False

import math

print(math.floor(3.5))
print(math.floor(-3.5))
print(math.floor(3.9))
# ? trunc gives us that value which is more towards the Zero.
print(math.trunc(2.8)) # 2.
print(math.trunc(-2.8)) # -2

import random

# ? random gives any random number between 0 and 1
print(random.random())


l1 = ["lemon", "masala", "ginger", "mint"]
print(random.choice(l1))

#? You can also shuffle this list in a random order using the random method

random.shuffle(l1)

print(l1)

# ! Python sometimes give wrong answers while doing zero precision calculation

print((0.1 + 0.1 + 0.1) - 0.3)

from decimal import Decimal

res = Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3")

print(res)


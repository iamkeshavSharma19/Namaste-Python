# ? Numbers and strings are widely used so what python does is it automatically does'not garbage collect them.Python takes some time to garbage collect it.

# ? Garbage Collection of strings and Numbers is little bit late inside the python.

a = 5
print(id(a))
b = 2
print(id(b))
a = a + 2
print(id(a))

# ! Let us talk about lists.
# ! Lists are mutable in Python.
myListOne = [1, 2, 3]
print(id(myListOne))
myListTwo = myListOne
print(id(myListTwo))
myListOne[0] = 33;
print(myListOne)
print(id(myListOne))
print(myListTwo)
print(id(myListTwo))

print("Experimenting More With Lists")

p1 = [1, 2, 3]
print(id(p1))
p2 = p1
print(id(p2))
p2 = [1, 2, 3]
print(id(p2))
p1[0] = 55
print(p1)
print(p2)

print("Playing More with Lists")
h1 = [1, 2, 3]
#?Here by doing slicing you have a separate copy of [1, 2, 3] and that separate copy is stored inside h2
h2 = h1[:]
print(id(h1))
print(id(h2))
#? '==' checks the value only.
print(h2 == h1)
#! 'is' checks the memory reference/address
print(h1 is h2)

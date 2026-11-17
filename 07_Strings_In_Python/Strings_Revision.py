name = "Brock Lesnar"
print("Brock Lesnar")

# name[0] = "D"
# print(name)

slice_name = name[0:5]
print(id(name))
print(id(slice_name))

#!THREE ADDRESSES WILL BE SAME.
# print(id(name[0:5]))
# print(id(name[0:5]))
# print(id(name[0:5]))

#?SLICING WILL ALWAYS MAKE A DIFFERENT COPY
#&Here memory address will be different.
a = name[0:5]
print(id(a))
b = name[0:5]
print(id(b))



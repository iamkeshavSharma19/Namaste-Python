name = "Harry Potter"
print(name)

first_char = name[0]
print(first_char)

# ? Now from "Harry Potter",I want to take out "Harry"
slice_name = name[0 : 5]
print(slice_name) #Harry
print(name) #Harry Potter

# ? Playing More with strings.
num_list = "0123456789"
print(num_list[:])

print(num_list[3:])
print(num_list[:7])
print(num_list[0:7:2])
print(num_list[0:7:3])

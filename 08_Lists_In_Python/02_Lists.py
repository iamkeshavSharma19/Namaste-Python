tea_varities = ["Black", "green", "Masala", "White"]
print(tea_varities)


print(tea_varities[1:1])
tea_varities[1:1] = ["test", "test"]
print(tea_varities)

print(tea_varities[1:2])
print(tea_varities[1:3])
#? Performing deletion as well.
tea_varities[1:3] = []
print(tea_varities)

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

#!LOOPS ON LISTS
for tea in tea_varities:
  print(id(tea))
  print(tea)

a = tea_varities[0]
print(id(a))
print(id(tea_varities[0]))


for tea in tea_varities:
  print(tea, end="-")
  
print("\n")
#~CONDITIONALS ON THE LISTS.

if "Oolong" in tea_varities:
  print("I have Oolong tea")
else:
  print("I donot have Oolong tea")
  
print(id(tea_varities))

a = tea_varities.append("Oolong")
print(a) #None
print(tea_varities)

print(id(tea_varities))
print(id(tea_varities[4]))

last_el = tea_varities.pop()
print(last_el)
print(id(last_el))

print(id(tea_varities))
tea_varities.remove("green")
print(tea_varities)
print(id(tea_varities))


#&INSERTING IN A LIST.
tea_varities.insert(1, "green")
print(tea_varities)

#!CREATING A NEW COPY OF LIST
tea_varities_copy = tea_varities.copy()

z = 1
print(id(z))
z = 1
print(id(z))

k = [1, 2]
print(id(k))
k = [1, 2]
print(id(k))

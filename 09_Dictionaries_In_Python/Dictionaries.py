user_info = {
  "firstName": "Keshav",
  "lastName": "Sharma",
  "age": 23
}

print(user_info)
print(id(user_info))

#? Accessing the individual items of the dictionary
print(user_info["firstName"])
print(id(user_info["firstName"]))
print(id(user_info["lastName"]))
print(id(user_info["age"]))

#?It provides the value of firstName
print(user_info.get("firstName"))
#?It provides the address/reference which is stored in firstName.
print(id(user_info.get("firstName")))

#?WE CAN ALSO CHANGE THE ITEMS OF THE DICTIONARY.
user_info["age"] = 20
print(user_info)
#!DICTIONARY IS MUTABLE,ON THE SAME MEMORY LOCATION FIELDS WILL CHANGE.
print(id(user_info))

#&Looping on the items of the Dictionary.
#&Here all the keys of the dictionary would be printed.
for key in user_info:
  print(key)

#~For printing the values
for info in user_info:
  print(info, user_info[info])


#*OTHER WAY OF LOOPING === specially if you are iterating on the dictionaries.
#* (key, value) === item.
for key, value in user_info.items():
  print(key, value)

if "firstName" in user_info:
  print("firstName is present")

print(len(user_info))


#!ADDING ONE MORE ITEM INSIDE THE DICTIONARY.
user_info["location"] = "Noida"
user_info["company"] = "Capgemini"

print(user_info)

#^SUPPOSE I WANT TO REMOVE AGE FROM MY DICTIONARY
print(user_info.pop("age"))
print(user_info)


#?Suppose If I want to remove the last item from my dictionary
print(user_info.popitem())
print(user_info)


#?del keyword removes the item from the memory location as well.
del user_info["location"]
print(user_info)

#?Copying the dictionary
user_info["location"] = "Noida"
user_info["company"] = "Capgemini"

print(user_info)

user_info_copy = user_info.copy()

print(id(user_info))
print(id(user_info_copy))

squared_num = {x:x**2 for x in range(6)}

print(squared_num)

#? Constructing a New Dictionary
keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"

new_dict = dict.fromkeys(keys, default_value)

print(new_dict)

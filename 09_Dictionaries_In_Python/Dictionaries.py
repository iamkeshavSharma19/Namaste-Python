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

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

#! Converting a string into lower case
print(name.lower())
#! Converting a string into upper case
print(name.upper())


friend = "      Ronald Weasely      "
print(friend)
#! For removing the extra spaces from the front and end
print(friend.strip())


#~ Here we are required to replace "Lemon" with "Ginger"
chai = "Lemon Chai"
print(chai.replace("Lemon", "Ginger"))


#& Converting a string into the List.For this we will use the split method.You also have to tell the split,on which basis split should happen.If you will not tell then It will split on it's own choice.
companies = "TCS, Wipro, HCL, Capgemini, Infosys"
print(companies.split())
print(companies.split(", "))

#!What if we want to find a word or a character in a string.
second_friend = "Hermoine Granger"
print(second_friend.find("e"))
#! If there is no word or a string which exists then It returns -1.
print(second_friend.find("z"))
#print(second_friend.find()) #!TypeError: find() takes at least 1 argument (0 given)

chai = "Masala Chai Chai Chai"
print(chai.count("Chai"))
print(chai.count("i"))
print(chai.count("Keshav"))

#? Adding the Placeholders inside the String.
chai_type = "Masala"
quantity = 2
order = "I order {} cups of {} chai"
print(order.format(quantity, chai_type))

#!CONVERTING LIST INTO THE STRING.
product_companies = ["Microsoft", "Uber", "Bloomberg", "Adobe", "ByteDance", "Oracle"]

print(product_companies)
print("".join(product_companies))
#?join doesnot changes the original list
print(product_companies)
print(" ".join(product_companies))
print("-".join(product_companies))
print("**".join(product_companies))
print(", ".join(product_companies))

#?How to print each character of the string
for letter in name:
  print(letter)

dialogue = "He said, \"Harry Potter is awesome\" "
print(dialogue)

# path = "c:\user\pwd"
# print(path) #!SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape

#!There are 2 ways of solving this issue ==> one is use '//' and the other is use r"", donot put \ at the end in this case
path = r"c:\user\pwd"
print(path)
path = "c:\\user\\pwd"
print(path)


print("Potter" in name)
print("P" in name)
print("Keshav" in name)





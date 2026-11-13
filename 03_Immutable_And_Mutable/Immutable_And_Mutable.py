# ? We have just studied that string is a immutable data type.
username = "Keshav"
print(username) # Keshav
#? Python has an inbuilt id function
print(id(username)) #1867379725568 === Address (reference)
username = "Brock"
print(username) #! Brock.But why String was immutable data type then why It is changing ??
print(id(username))
user_info = "Keshav"
print(id(user_info))
user_detail = "Keshav"
print(id(user_detail))


x = 10
y = x
print(x) #10
print(id(x))
print(y) #10
x = 15
print(x) #15
print(id(x))
print(y) #10 

# ^In Python, everything is made as an object.
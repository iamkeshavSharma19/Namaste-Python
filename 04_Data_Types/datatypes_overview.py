username = "Keshav"
print(len(username))
print(username[0])
# username[0] = "A" TypeError: 'str' object does not support item assignment

print(username[-1]) #?When we put negative sign it starts counting from the backwards
#! print(username[7]) IndexError: string index out of range
#! print(username(-7)) TypeError: 'str' object is not callable
print(username[1:3]); #?start from index 1 but donot include 3
mylist = [123, "chai", 3.14]
print(mylist)
print(mylist[0])
print(mylist[-1])
myDic = {
  "one": "Lemon",
  "two": "ginger",
  "comic": "naagraj"
}
print(myDic)
print(myDic["comic"]);

# print(myDic["comics"]);KeyError: 'comics'
myTup = (1, 2, 4)
print(myTup[0])

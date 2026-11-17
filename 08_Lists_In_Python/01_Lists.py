companies = ["TCS", "Wipro", "Infosys", "Capgemini"]
print(id(companies))



print(companies)
print(companies[3])
print(companies[-1])
print(companies[1:3])
print(companies[:2])
print(companies[2:])
companies[1] = "Tech Mahindra"
print(companies)

#? reference of companies and slice_companies will be different.
slice_companies = companies[1:3]
print(id(companies))
print(id(slice_companies))

print("_______________________________________________")



# print(companies[1:2]) #?["Tech Mahindra"]

tech_mahindra = companies[1:2]
print(id(companies))
print(id(tech_mahindra))
print(id(companies[1:2]))
companies[1:2] = "Wipro"
print(companies)
print(id(companies))
print(tech_mahindra)
print(id(tech_mahindra))

#? Slicing always make a new list object.
print("________________________________________________")
#! Every time we will perform slicing, everytime python makes a new List Object.The memory address of all these 3 will be different.Whenever we perform slicing and the slicing syntax is on the right hand side of equality,then evertime a new list object will be made inside the memory,original list will not change.
print(id(companies[1:2]))
print(id(companies[1:2]))
print(id(companies[1:3]))
print(companies[1:2] == companies[1:2])
print(companies[1:2] is companies[1:2])


a = companies[1:2]
print(id(a))
b = companies[1:2]
print(id(b))
c = companies[1:2]
print(id(c))


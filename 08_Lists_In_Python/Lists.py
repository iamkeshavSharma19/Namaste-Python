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


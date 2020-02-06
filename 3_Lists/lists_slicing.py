# Indexing a list

countries = ["Brazil", "Japan", "Colombia", "Slovakia", "Mexico", "Canada", "USA", "Korea"]

print(countries[-1])
print(countries[0])
print(len(countries))

# Modigy (change, mutate) elements (Lists are MUTABLE)
countries[-1] = "South Korea"
print(countries)

# Slicing lists (end index is not inclusive)
print(countries[0:3])
countries[5:8] = []
print(countries)
countries[0:3] = ["U.N"]
print(countries)
print(countries[:3])
print(countries[3:])

print(["2", "3"] * 3)


# d = {key1:value1, key2:value2, key3:value3,…}
astro_obj = {"earth": 1, "mars": 2, "halley": 3} 
# astro_obj is a dictionary with “earth”, “mars”, and “halley” as its keys,
# and the corresponding values are 1, 2, and 3, respectively.
print(astro_obj) # {'earth': 1, 'mars': 2, 'halley': 3}
print(astro_obj["mars"]) # 2

astro_obj["sun"] = "s"
print(astro_obj) # {'earth': 1, 'mars': 2, 'halley': 3, 'sun': 's'}

astro_obj["earth"] = 0
print(astro_obj) # {'earth': 0, 'mars': 2, 'halley': 3, 'sun': 's'}

del astro_obj["earth"]
print(astro_obj) # {'mars': 2, 'halley': 3, 'sun': 's'}

print("mars" in astro_obj) # True
print("earth" in astro_obj) # False
print("earth" not in astro_obj) # True

print(len(astro_obj)) # 3

a = dict.copy(astro_obj)
print(a) # {'mars': 2, 'halley': 3, 'sun': 's'}
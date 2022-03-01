ages = [5, 15, 64, 27, 84, 26]

odd_ages = [age for age in ages if age % 2 != 0]
print(odd_ages)

chickens = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]
long_chicken_names = [chicken for chicken in chickens if len(chicken) >10 ]
print(long_chicken_names)
h_chicken_names = [chicken for chicken in chickens if chicken[0].lower() == "h"]
print(h_chicken_names)

words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
first_letter = [word[0].lower() for word in words]
print(first_letter)
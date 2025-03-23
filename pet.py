pets = []

pet = {"dog" : "billy", "cat" : "bob", "bird" : "bong"}

pets.append(pet)

for pet in pets:
    print("Pet Details")
    for animal, name in pet.items():
        print(f"{animal.capitalize()} name is {name}")
    print()
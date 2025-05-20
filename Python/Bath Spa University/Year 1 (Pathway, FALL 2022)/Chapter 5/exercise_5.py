pet1 = {"animal": "dog", "owner": "Patrick"}
pet2 = {"animal": "cat", "owner": "Spongebob"}
pet3 = {"animal": "crocodile" ,"owner": "Mr. Krabs"}

# Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.
pets = [pet1, pet2, pet3]
for pet in pets:
    print(f"The pet is an animal called {pet['animal']}. His owner is {pet['owner']}.")
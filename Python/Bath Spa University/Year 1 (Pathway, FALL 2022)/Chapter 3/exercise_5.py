guests = ["Antonio", "Miguel", "Intal"]

print(f"It's so sad {guests.pop(0)} couldn't make it. Oh well, I will invite someone else on my list!")

guests.insert(0, "Jo")
for guest in guests:
    print(f"Greetings, {guest}! I would like to invite you to my dinner!")
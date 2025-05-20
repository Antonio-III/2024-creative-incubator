ALLOWED_GUESTS = 2
EMPTY = 0

guests = ["Antonio", "Miguel", "Intal"]

print(f"My new dinner table couldn't arrive in time, so I can only have {ALLOWED_GUESTS} guests for my dinner!")

# Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.		
while len(guests) > ALLOWED_GUESTS:
		print(f"I'm so sorry, {guests.pop()}. I can only host 2 guests for my dinner!")

# Print a message to each of the two people still on your list, letting them know they’re still invited.
for guest in guests:
    print(f"Hello, {guest}! You're still invited to my dinner!")
    
# Use del to remove the last two names from your list, so you have an empty list.
while len(guests) != EMPTY:
	del guests[0]

# Print your list to make sure you actually have an empty list at the end of your program.
print(guests)
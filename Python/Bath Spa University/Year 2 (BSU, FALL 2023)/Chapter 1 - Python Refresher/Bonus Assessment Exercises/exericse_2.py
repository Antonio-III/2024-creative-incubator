# Newlines will be added for a cleaner output

def main() -> None:
	# We initialize the given list
	locations =['dubai','paris', 'switzerland', 'London', 'amsterdam', 'New York']

	# 1. We print the list as is and its length
	locations_len = len(locations)
	print(f"The list contains: {locations}. And the length of this list is {locations_len}! \n")

	# 2. We sort the list
	locations_sorted = sorted(locations)
	print(f"When we use the 'sorted()' function on our list, we get will this list: {locations_sorted}! \n")

	# 3. We will show the original list. The 'sorted()' function does not modify the list itself, rather it returns a different iist but sorted based on the one we passed
	print(f"The original list remains intact. As a matter of fact, here it is!: {locations}! \n")

	# 4. We will sort the list in reverse order
	locations_sorted_reverse = sorted(locations, reverse = True)
	print(f"The list in reverse alphabetical order is.. {locations_sorted_reverse}! \n")

	# 5. Print the original list. The og list is still unaffected
	print(f"The list is still intact! Here it is!: {locations}! \n")

	# 6. Use the '.reverse()' method. This will arrange the list in reverse order (not ascending or descending), and modify the og list and it returns 'None'
	locations.reverse()

	# 7. Print the og list
	print(f"The list has now been permanently reversed! This is now the original list: {locations}! \n")

	# 8. Use '.sort()' method to sort the list in ASCII-betical order
	locations.sort()

	# 9. Print the list
	print(f"The old order of the list is gone, it is now sorted not in reverse, but in ascending order (In terms of its ASCII value)!...: {locations}! \n")

	# 10. Use '.sort()' but make it so the it arranges it from reverse ASCII-betical order
	locations.sort(reverse=True)

	# 11. Print the list
	print(f"And for my last trick, I will sort the list in reverse ASCII-betical order (Descending ASCII values)!... This is it!: {locations}! \n")

if __name__ == "__main__":
	main()
# We intialize the 'marks' variable
MARKS = [("CodeLab I", 67), ("web Development", 75), ("CodeLabII", 74), ("Smartphone Apps", 68), ("Games Development", 70), ("Responsive web", 65)]

SECOND_ELEMENT = 1

def main() -> None:
	print(f"This is the 'marks' variable by default!: {MARKS} \n")

	# We will use the 'sorted()' function with a custom key to sort by their tuple's second elements
	marks_descending = sorted(MARKS, key = lambda items: items[SECOND_ELEMENT], reverse = True)
	print(f"This is 'marks' arranged in descending by their second elements!: {marks_descending} \n")

	# We will sort by ascending, but using the same custom key
	marks_ascending = sorted(MARKS, key = lambda items: items[SECOND_ELEMENT])

	print(f"This is 'marks' arranged in ascending order by their second elements!: {marks_ascending} \n")

if __name__ == "__main__":
	main()
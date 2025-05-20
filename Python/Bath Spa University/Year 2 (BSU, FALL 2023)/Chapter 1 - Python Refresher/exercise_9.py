# Import these two functions (seed and randint) from the 'random' module. This is so that we can make a list with different variables for every run of the code
from random import seed
from random import randint

ZERO = 0
ONE = 1
TWO = 2
TEN = 10
ONE_HUNDRED = 100

def main() -> None:

	# We seed the later random number generator by giving it a random number from 0~10. If we do not give a seed to a random number generator like this (line 15) for instance, the seed of will be the current system time in seconds or milliseconds. This will determine what integer our 'seed()' will get
	seed(randint(ZERO, TEN))

	# 1. Initialize a list with 10 values with random numbers. Random numbers are determined by the integer the 'seed()' (line 15) has, and the integer's seed is determined by the current system time
	int_list = [randint(ZERO, ONE_HUNDRED) for _ in range(TEN)]

	# 2. We output the list using a 'for loop'. It has 10 values so we will loop for 10 times
	index_to_print = 0 # We create a variable to be incremented by 1 to be used in the 'for loop'
	print("This is the list as it is:", end = " ") # We change the 'end' value so that the numbers will be output in the same line as this statement
	for _ in range(TEN):
		print(int_list[index_to_print], end = ", ") # We change the 'end' value here as well so that the numbers are separated by a comma (,) and space ( ) instead of a newline (\n)
		index_to_print+=1

	print("\n") # Create 2 newlines. Output ends with a newline by default. This will make it so that there is 1 empty space gap for every output

	# 3. To output our highest value, we use the 'max()' function. To output our lowest value, we use the 'min()' function
	highest_value = max(int_list)
	lowest_value = min(int_list)
	print(f"The highest number in our 'int' list is '{highest_value}' and the lowest is '{lowest_value}'! \n")


	# 4. To sort the elements in ascending order
	sorted_list_asc = sorted(int_list)
	print(f"This is the sorted list in asncending order: {sorted_list_asc}. \n")

	# 5. To sort the elements in descending order
	sorted_list_desc = sorted(int_list, reverse = True)
	print(f"This is the sorted list in descending order: {sorted_list_desc}. \n")

	# 6. For appending two elements, I will use a the 'randint()' function
	for _ in range(TWO):
		int_list.append(randint(ZERO, ONE_HUNDRED))

	# 7. Then we print the list itself after appending
	print(f"This is the list after appending 2 elements: {int_list}.")

if __name__ == "__main__":
	main()
FIRST_ELEM = 0
SECOND_ELEM = 1
THIRD_ELEM = 2

def main() -> None:
	three_nums = {"first": 0, "second": 0, "third": 0} # Initialize a dict that will collect the 3 numbers entered

	for n in three_nums.keys(): # This for loop iterates as much as the amount of items in the list (3)
		entered_num = int(input(f"Input the {n} number: \n")) # Turns the input into an integer and store it into the variable
		three_nums[n] = entered_num # Add the entered nunmbers as the keys' value

	# Sort the dictionary by their values-pair in descending order by using a custom sorting key. This returns a list-type so we use dict() to convert the list into a dict-type. We need to keep it dict-type as we'll use this variable later. 

	# The lambda function is how we're going to sort the dictionary. In our case, we wrote 'item[1]' which sorts it by the second element. Since we will retrieve the .items() of the dictionary instead of just the dictionary itself, it will be sorted by the second element in the first item, which happens to be the values-pair of the dictionary. This is because when we retrieve the .items() of a dict, it returns a list (from sorted()) and within that list, a tuple for each key-value pair of the dictionary. 

	# If we don't retrieve the .items(), and we remove the conversion to a dict (it causes errors), this returns a list (from sorted()) and inside the list are strings (the key-pairs). And the 'item[1]' will sort it by the second element of the first item, being the second letter of 'first'.

	sorted_nums = dict(sorted(three_nums.items(), key = lambda item: item[1], reverse = True))

	# Store the variable keys and values to these variables. 'desc' means 'descending'
	desc_num_keys, desc_num_values = zip(*sorted_nums.items())

	# Find the greatest number in the list using multiple if-else statements. This automatically finds the the highest entered number, along with its associated key. Both conditions must be true for the code under to execute.
	one_num_greatest = desc_num_values[FIRST_ELEM] > desc_num_values[SECOND_ELEM] and desc_num_values[FIRST_ELEM] > desc_num_values[THIRD_ELEM]

	all_nums_equal = desc_num_values[FIRST_ELEM] == desc_num_values[SECOND_ELEM] and desc_num_values[FIRST_ELEM] == desc_num_values[THIRD_ELEM]

	if one_num_greatest:
		print(f"The {desc_num_keys[FIRST_ELEM]} number is the greatest, being {desc_num_values[FIRST_ELEM]}.") # Outputs the greatest number as well as their position in the list
		
	# All numbers are equal
	elif all_nums_equal:
		print(f"All numbers are equal, that being {desc_num_values[FIRST_ELEM]}.")

	# There are 2 greatest numbers
	else:
		print(f"The {desc_num_keys[FIRST_ELEM]} and {desc_num_keys[SECOND_ELEM]} numbers are both the greatest, being {desc_num_values[FIRST_ELEM]}.")

if __name__ == "__main__":
	main()
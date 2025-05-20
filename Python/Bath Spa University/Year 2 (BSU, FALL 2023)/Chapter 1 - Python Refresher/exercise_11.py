def main() -> None:
	# 1. We create the tuple 
	year = (2017,2003,2011,2005,1987,2009,2020,2018,2009)

	# 2. We access the value at the given index (-3)
	print(f"The 3rd-to-the-last number in the tuple is: {year[-3]}! \n") # This prints the 3rd-to-the-last value

	# 3. To reverse the tuple, we will use a slicing notation([::]). Tuples are immutable, so we can't directly modify it. But what we can do is create a copy of the tuple and order sort in a reverse order (in terms of index positions)
	reverse_year = year[::-1]

	print(f"This is the original tuple: {year}.") # We print the original and the reversed copy 
	print(f"And this is the reversed tuple: {reverse_year}. \n")

	# 4. We will use '.count()' to see how many elements match the integer '2009'
	times_2009_appeared = year.count(2009)
	print(f"The number of times '2009' has appeared in the tuple is: {times_2009_appeared}! \n")

	# 5. We will use '.index()' to get the index value of the integer '2018'
	index_2018 = year.index(2018)
	print(f"The index value of '2018' in the tuple is: {index_2018}!")
	print(f"This means that the number is in the {index_2018}th position! \n")

	# 6. We will use len to find out how many elements are in the tuple
	year_len = len(year)
	print(f"The length of the 'year' tuple is: {year_len}!")
	print(f"This means there are {year_len} elements in the tuple!")

if __name__ == "__main__":
	main()
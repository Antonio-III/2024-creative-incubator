# Write a program that prints the even numbers from 1 to 100. 
# Hint - Use Continue Statement

ONE = 1
TWO = 2
ONE_HUNDRED = 100

def main() -> None:
	# create a 'for loop' that iterates over a range containing numbers 1~100
	for num in range(ONE, ONE_HUNDRED + ONE):
		# if the current value of num, when divided by 2, returns 0, it will print the number
		num_divisible_by_2 = not (num % TWO)
		if num_divisible_by_2: 
			print(num)
		# if it fails the above condition, it will go back to the top of the loop (we use 'continue' statement here because python expects an indented code block)
		else:
			continue

if __name__ == "__main__":
	main()
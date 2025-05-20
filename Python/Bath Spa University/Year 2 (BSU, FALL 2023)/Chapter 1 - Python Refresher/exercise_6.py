ONE = 1
THREE = 3
FIVE = 5
ONE_HUNDRED = 100

def main() -> None:
	# Create 'for loop' that iterates in a range function that contains the numbers from 1~100 
	for num in range (ONE, ONE_HUNDRED + ONE):

		# We use modulo division to check if the 'num' variable would be a multiple of a number (3 and 5). if the return is 0, it is indeed a multiple
		# We put this condition first because we need to make sure that if the number is a multiple of 15, this line (line 17) would execute first
		num_divisible_by_3 = not (num % THREE)
		num_divisible_by_5 = not (num % FIVE)
		
		if num_divisible_by_3 and num_divisible_by_5:
			print("FizzBuzz")
			
		elif num_divisible_by_3:
			print("Fizz")
			
		elif num_divisible_by_5:
			print("Buzz")

		# If the iteration fails all the above conditions, it means it is not a multiple of 3 or 5, or both; so we print the number instead
		else:
			print(num)
			
if __name__ == "__main__":
	main()
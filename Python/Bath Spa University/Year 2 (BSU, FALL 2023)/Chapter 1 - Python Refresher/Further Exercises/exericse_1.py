HOURS_IN_A_DAY = 24
MINUTES_IN_AN_HOUR = 60 
SECONDS_IN_A_MINUTE = 60

LOWERCASE_Y = 'y'
LOWERCASE_N = 'n'

def main() -> None:
	print("In this exercise, we will turn the amount of days you give into seconds! \n")

	# Initialize boolean to be used later
	exit_loop = False

	while exit_loop == False:
		
		# Initialize an input variable
		days = int(input("Enter the amount of days: \n"))
		
		days_to_seconds = days * HOURS_IN_A_DAY * MINUTES_IN_AN_HOUR * SECONDS_IN_A_MINUTE
		
		print(f"The amount of seconds in the amount of days you entered is...{days_to_seconds}! \n")
		
		while True:
			
			try_again = input("Would you like to continue? (y/n) \n") # We put this code inside the second loop because we want to keep asking the user if they would like to continue if they keep entering an invalid character
			
			if try_again == LOWERCASE_Y:
				break

			elif try_again == LOWERCASE_N:
				exit_loop = True
				break

			else:
				print("Invalid character")

if __name__ == "__main__":
	main()
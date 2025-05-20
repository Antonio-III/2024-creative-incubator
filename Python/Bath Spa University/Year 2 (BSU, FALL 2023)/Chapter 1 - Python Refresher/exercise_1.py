def main() -> None:
	name = input("Hello, user!\nWhat is your name? \n") # no whitespace between \n and "What" because it creates a blank space in the output
	age = int(input("What is your age? \n")) # you can use \n like this here because there is no letter after the \n that messes up the formatting
	name_len = len(name) # to store the length of the name
	age_one_year = age + 1 # used a variable to store so that all print functions use f-string formatting

	print(f"It is good to meet you, {name.title()}!") #used .title() method to capitalize the first letters of the name
	print(f"The length of your name is: \n{name_len}")
	print(f"You will be {age_one_year} in a year.")
	
if __name__ == "__main__":
	main()
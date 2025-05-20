ZERO = 0
THREE = 3
TWELVE = 12

def main():
	while True:
		age = int(input("Enter your age. Your movie ticket will be based on how old you are. Enter '0' to stop: \n"))
		if age == ZERO:
			break
		elif age < THREE:
			print("Your movie ticket costs free.")
		elif age >= THREE and age < TWELVE:
			print("Your movie ticket costs $10.")
		else:
			print("Your movie ticket costs $15.")
		
if __name__ == "__main__":
	main()
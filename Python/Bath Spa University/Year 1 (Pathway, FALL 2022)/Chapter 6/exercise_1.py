def main():
	while True:
		topping = input("Enter a pizza topping or enter 'quit' to stop: ")
		if topping == "quit":
			break
		else:
			print(f"You have entered {topping} as a pizza topping!")
			
if __name__ == "__main__":
	main()
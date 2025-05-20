def main():
	sandwich_orders = ["Tuna sandwich", "Grilled cheese", "Ham sandwich", "Chicken sandwich", "Egg sandwich"]
	# Then make an empty list called finished_sandwiches.
	finished_sandwiches = []
	# Loop through the list of sandwich orders and print a message for each order, such as: "I made your tuna sandwich."
	while True:
		print(f"Here are the sandwiches in my recipe: {sandwich_orders} enter ctrl-C to exit.")
		order = input("Enter your order in my recipe\n")
		if order in sandwich_orders:
			print(f"I made your {order}.")
			# As each sandwich is made, move it to the list of finished sandwiches.
			finished_sandwiches.append(order)
			# After all the sandwiches have been made, print a message listing each sandwich that was made.
			if len(sandwich_orders) == len(finished_sandwiches):
				order = input(f"You entered all the sandwiches in my recipe! Enter 'y' to try again.\n")
				if order == "y":
					sandwich_orders = finished_sandwiches
					finished_sandwiches = []
					continue
				else:
					break
		elif order in finished_sandwiches:
			print("I already made that sandwich! Try again!")
			
		else:
			print(f"That's not in my recipe! Try again!")
			
if __name__ == "__main__":
	main()
ZERO = 0 

def main():
	sandwich_orders = ["Pastrami sandwich", "Pastrami sandwich", "Pastrami sandwich", "Tuna sandwich", "Grilled cheese", "Ham sandwich", "Chicken sandwich", "Egg sandwich"]
	finished_sandwiches = []
	print("The deli has run out of pastrami sandwich! Sad!")
	while sandwich_orders.count("Pastrami sandwich") > ZERO:
		sandwich_orders.remove("Pastrami sandwich")
		print(f"Here are the sandwiches in my recipe: {sandwich_orders}")
		print(f"Finished sandwiches: {finished_sandwiches}")
		
if __name__ == "__main__":
	main()
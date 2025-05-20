ONE = 1
TEN = 10

def main() -> None:
    # Create a loop that ranges from numbers 1~10. This will determine the amount of rows we have, and the first factor for our multiplication
    for x in range(ONE, TEN + ONE):
        print(f"This is the table of {x}!")

        # We create a nested loop ranging from numbers 1~10. This determines the numbers we will print. We will only use 1 column as well, so we will not be changing the 'end' argument of 'print()'
        for y in range(ONE, TEN + ONE):
            print(f"{x} x {y} = {x*y}")

    # We put a 'print()' statement to create an empty space after the 'y' iteration finishes
    print()

if __name__ == "__main__":
	main()
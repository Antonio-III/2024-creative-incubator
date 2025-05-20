# We import these functions as we will use them again for this exercise
from random import seed
from random import randint

ZERO = 0
ONE = 1
THREE = 3
TEN = 10

def list_product(my_list: list[int]) -> int:
    
    # We will call the 'seed()' function to seed our 'randint()' functions. The seed of 'randint()' function inside 'seed()' will be the current system time  
    seed(randint(ZERO, TEN))

    # Initialize a counter for the total product. Putting this variable outside the function will not work because since we will call this variable later on (line 19), Python thinks that we are referring to a local variable (a variable inside the function) with the same name, of which doesn't exist, and so will cause an error
    product = 1

    print(f"These are the numbers in that list: {my_list}! \n")
    
    for i in my_list:
        
        # We can use a variable's previous value and assign it to the same variable, which will replace the old one
        product = product * i
        
    return product


def main() -> None:
	rand_list = [randint(ONE, TEN) for _ in range(THREE)]

	print(f"And the product of all the numbers is... {list_product(rand_list)}!")

if __name__ == "__main__":
	main()
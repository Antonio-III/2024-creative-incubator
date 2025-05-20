LOWERCASE_Y = 'y'
LOWERCASE_N = 'n'

# We will initialize a boolean variable as we will need to control the flow of the loops later on. We will use 2 loops, a main one, and a nested
OUTER_LOOP = True
INNER_LOOP = True

def take_response(response: str) -> None:
  global OUTER_LOOP # The names after the keyword 'global' are referring to the global variables. Meaning the variable is defined outside the function
  global INNER_LOOP
  function_loop = True # This is a local variable. Meaning it is only defined inside the function. The only reason why we have this is for the 'else' section of the function

  while function_loop == True:
    if response == LOWERCASE_Y:
      INNER_LOOP = False # This means for the next iteration, the inner loop's condition would be false
      function_loop = False # This means that we will not run the next iteration of this function, causing us to exit the function since there is none left to execute (notice how this 'while loop' is the last main code-block in the function)

    elif response == LOWERCASE_N:
      # We fail all the conditions of all the loops so that we exit all the loop code-blocks in the next iteration (there won't be any)
      INNER_LOOP = False
      OUTER_LOOP = False
      function_loop = False

    else:
      response = input("Invalid response! Would you like to try again? (y/n) \n") # I used a local variable here because we want the function to keep updating the value of its local variable so that the user can eventually exit this function's loop (If they give a valid character). I got stuck in this section because I used the global var 'response'

def main() -> None:
    global OUTER_LOOP
    global INNER_LOOP

    # Initialize a string list of names be checked which input is valid
    staff = ["Arshiya", "Usman", "Iftikhar", "Usman","Rafia", "Mary", "Anmol","Zainab","Iftikhar", "Arshiya","Rafia","Jake"]

    print(f"For this exercise, we will count the amount of times a specific name appears in the list!\n")

    while OUTER_LOOP == True:
        
        # Initialize this boolean var (INNER_LOOP) inside the main 'while loop' so that its value resets per iteration
        INNER_LOOP = True
        
        name = input("Enter whose name you'd like to count: 'Arshiya', 'Usman', 'Iftikhar', 'Rafia', 'Mary , 'Anmol', 'Zainab', 'Jake' \n")

        # We turn the input name into uppercase so that if it's a lowercase input, it is still valid
        input_name = name.title()

        # Check if the uppercased input matches any items in the list
        if input_name in staff:
            
            # Store the count inside a variable for efficiency (we don't have to type 'staff.count(input_name)' repeatedly)
            name_count = staff.count(input_name)
            
            print(f"The amount of times the name '{input_name}' appears on the list is... {name_count}!!! \n")
            print(f"The list: {staff}\n")
            response = input("That's all for this program! Would you like to try again? (y/n) \n")

            # We call on the function, passing an input var as the argument 
            take_response(response)

        else:
            while INNER_LOOP == True:
                response=input("That name is not on the list, would you like to try again? (y/n) \n")
                take_response(response)

    print("Thanks for playing!")

if __name__ == "__main__":
	main()
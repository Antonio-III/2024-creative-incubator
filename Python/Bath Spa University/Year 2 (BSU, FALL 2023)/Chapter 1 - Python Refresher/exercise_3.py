# Start of program
TRIANGLE_SIDES = 3
A = 0
B = 1
C = 2
    
def main() -> None:
	entered_triangle_sides = 0 # A counter to see how many sides have been input
	triangle_sides = [] # Created a list to store all the sides that have been input 

	while entered_triangle_sides < TRIANGLE_SIDES: # Runs a loop to run the code below repeatedly
		triangle_side = int(input("Enter a triangle side:\n"))
		triangle_sides.append(triangle_side) # Adds the input number to the list
		entered_triangle_sides = entered_triangle_sides +1 # Once the code above has been executed, this will add a +1 to the variable on line 8
		

	# Checks if the input sides pass the triangle inequality theorem
	side_a_b_at_least_gt_c = triangle_sides[A] + triangle_sides[B] > triangle_sides[C]
	side_b_c_at_least_gt_a = triangle_sides[B] + triangle_sides[C] > triangle_sides[A]
	side_c_a_at_least_gt_b = triangle_sides[C] + triangle_sides[A] > triangle_sides[B]

	if side_a_b_at_least_gt_c and side_b_c_at_least_gt_a and side_c_a_at_least_gt_b:
		
		print("You have entered a triangle! Congratulations!") # The input sides must pass the triangle inequality theorem for this to execute
		
		
		# This is for the extension problem. This executes if the condition (line 25) is met
		side_a_b_equal = triangle_sides[A] == triangle_sides[B]
		side_b_c_equal = triangle_sides[B] == triangle_sides[C]
		side_c_a_equal = triangle_sides[C] == triangle_sides[A]
		if side_a_b_equal and side_b_c_equal:
			print("And you entered an Equilateral Triangle!")
		
		elif side_a_b_equal or side_b_c_equal or side_c_a_equal:
			print("And you entered an Isosceles Triangle!")
			
		else:
			print("And you have entered a Scalene Triangle!")
		
	else: 
		print("This is not a valid triangle! :((\nSad!")

if __name__ == "__main__":
	main()
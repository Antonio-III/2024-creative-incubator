ONE = 1
SIX = 6

def main() -> None:
	# Create the first 'for loop'. This first loop represents the amount of rows we will have (5). We use the arguments '1,6' since we will use the values later on  
	for rows in range(ONE, SIX):
	
		for columns in range(ONE, rows + ONE): # This nested 'for loop' will represent the printed values in every column. We start from 1 until the current value of 'x'. This means that we will print '1' in the first iteration, then '1 2' in the second and so on. This will be a problem because every 'print()' by-default ends on a newline (\n) 
			
			print(columns, end = " ") # We use the 'end' argument to replace the default 'end' value which is a newline character (\n). This is so that the values we print will all be on the same line, with an empty space ( ) in between. This will create a problem since there is no separation for every iteration, but we will address it later on
		
		print() # We call on the 'print()' statement here because as I wrote, it has a default newline character (\n) after the output. Since there is no output, it will only include the newline character. This is placed outside of the nested loop because we want the nested loop's values to print as they are, but we want to separate the iterations by letting them start on a new line, thus creating the pattern, so it is placed after the execution of the nested loop

if __name__ == "__main__":
	main()
ROWS = 8
ROWS_IN_FIRST_HALF_OF_ARROW = 5

def main() -> None:
    def create_first_half_of_arrow(row: int) -> None:
        nonlocal times
        spaces = " " * times
        star = "*" * (row * 2 + 1)
        print(spaces + star)

        times -= 1

        return None
    def create_last_half_of_arrow() -> None:
        spaces = " " * 3
        star  = "*" * 3
        print(spaces + star)    
            
        return None
    
    # Create a loop. This will be the amount of rows we have. We will not create a nested loop because we will not need it. Every iterations end in a new line and inside those iterations are our 'columns'
    times = 4

    for row in range(ROWS):
        if row < ROWS_IN_FIRST_HALF_OF_ARROW:
            create_first_half_of_arrow(row)   
        else:
            create_last_half_of_arrow()
            


if __name__ == "__main__":
	main()
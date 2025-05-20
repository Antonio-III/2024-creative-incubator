# For this exercise, we will make a function

ZERO = 0
TEN = 10

def sum_of_digits(number: int) -> int:
    current_sum = 0
    
    while number > ZERO:
        current_sum += number % TEN # We will collect the number in the ones-place from the tens-place, hundreds, etc... And store it in a variable

        number = number // TEN # We remove the current ones-place because it has already been added to the 'sum' variable. We use modulo division because normal division counts the decimal, modulo only counts the whole number, which is how 'number' will eventually reach 0. 

    return current_sum
  
def main() -> None:
	num = int(input("Enter a number, and this program will find the sum of its digits! \n"))
      
	print(f"The sum of the digits in {num} is... {sum_of_digits(num)}!")

if __name__ == "__main__":
	main()
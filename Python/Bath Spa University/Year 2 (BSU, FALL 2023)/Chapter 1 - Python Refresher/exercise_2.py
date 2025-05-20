def main() -> None:
	first_num = int(input("Enter a number \n"))
	second_num = int(input("Enter a second number \n"))

	sum = first_num + second_num
	diff = first_num - second_num
	prod = first_num * second_num
	quo = first_num / second_num
	rem = first_num % second_num

	print(f"The sum of the numbers is: {sum}!")
	print(f"The difference of the numbers is: {diff}!")
	print(f"The product of the numbers is: {prod}!")
	print(f"The quotient of the numbers is: {quo}!")
	print(f"The remainder of the numbers is: {rem}!")

if __name__ == "__main__":
	main()
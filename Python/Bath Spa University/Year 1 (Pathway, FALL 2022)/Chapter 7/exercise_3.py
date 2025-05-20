def make_shirt(size: int, text: str) -> None:
    print(f"The size of the shirt is {size} and the text printed on it is '{text}'.")
	
def main() -> None:
	t_shirt_size = 12
	t_shirt_text = "bruh"
	
	# Call the function once using positional arguments to make a shirt.
	make_shirt(t_shirt_size, t_shirt_text)
	# Call the function a second time using keyword arguments.
	make_shirt(size = t_shirt_size, text = t_shirt_text)
	
if __name__ == "__main__":
	main()
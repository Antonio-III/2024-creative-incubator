def make_shirt(size: str = "large", text: str = "I love python") -> None:
    print(f"The size of the shirt is {size} and the text printed on it is '{text}'.")

def main() -> None:
	#Make a large shirt
	make_shirt()
	# and a medium shirt with the default message,
	make_shirt("medium")
	# and a shirt of any size with a different message.
	make_shirt("small", "different message")
	
if __name__ == "__main__":
	main()
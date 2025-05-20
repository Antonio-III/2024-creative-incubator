def describe_city(city: str, country: str = "UAE"):
    print(f'The city called "{city}" is in the country called "{country}".')

def main() -> None:
	describe_city("Abu Dhabi")
	describe_city("Dubai")
	describe_city("Amsterdam", "Netherlands") 
	
if __name__ == "__main__":
	main()
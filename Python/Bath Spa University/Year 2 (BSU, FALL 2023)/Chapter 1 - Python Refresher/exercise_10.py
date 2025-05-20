def main() -> None:
	# We create a dictionary that stores data about the movie "Inception"
	film_details = {"Title": "Inception", 
					"Director": "Christopher Nolan", 
					"Year of release": 2010,
					"Rating" : 8.8,
					"Box Office" : "839 million"
				}
	# We display the contents (keys and values) of the dictionary 
	for keys, values in film_details.items():
		if keys == "Title":
			print(f"The Movie's {keys} is {values}", end = ". ") # The 'end' argument will replace the default newline character (\n) with a period and a space (. ). This is just for a cleaner output
		else:
			print(f"The {keys} is {values}", end = ". ") # The printed statement here is slightly different. This is so that the all the printed sentences look continuous

if __name__ == "__main__":
	main()
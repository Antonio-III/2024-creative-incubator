def main():
    speech=input("What do you want to say?\n")
    print(slowed(speech))

# replace any occurrences of whitespace in the string to a ...
def slowed(words):
    return words.replace(" ","...")

def test(function):
    print(function("This is CS50"))
    print(function("This is our week on functions"))
    print(function("Let's implement a function called hello"))

test(slowed)

main()

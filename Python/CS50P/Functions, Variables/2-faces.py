# Turn any :) to 🙂 and :( 🙁

def main():
    text=input("Enter a text and include a basic emoticon! \n")
    print(convert(text))

def convert(to):
    return to.replace(":)","🙂").replace(":(","🙁")

def test(function):
    print(function("Hello :)"))
    print(function("Goodbye :("))
    print(function("Hello :) Goodbye :("))


test(convert)

main()
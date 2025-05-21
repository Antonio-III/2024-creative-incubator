def main():
    # prompt user for an input
    sentence=input("What do you want to say?\n")

    # output the input in lowercase
    print(indoor_voice(sentence))

def indoor_voice(voice):
    return voice.lower()

# test cases
def test(function):
    print(function("HELLO"))
    print(function("THIS IS CS50"))
    print(function("50"))

test(indoor_voice)

main()
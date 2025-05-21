# Prompt an input() to represent a mass, and output the Energy in joules.

def main():
    print(output_joules())


def output_joules(mass=int(input("Enter mass: "))):
    return f"Energy: {mass*300000000**2}"

def test(function):
    print("Testing Function...")
    print(function(mass=1))
    print(function(mass=14))
    print(function(mass=50))

test(output_joules)

main()
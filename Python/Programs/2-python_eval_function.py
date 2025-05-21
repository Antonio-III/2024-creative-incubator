# Python script that returns a value after passing it to the eval() function. This is supposed to be my offline calculator.
import typing

OPEN_PARENTHESIS = "("
CLOSING_PARENTHESIS = ")"
MULTIPLY_X = "x"
MULTIPLY_SIGN = "*"

def main() -> None:
    try:
        equation = input("Enter equation: ").replace(MULTIPLY_X, MULTIPLY_SIGN)
    except KeyboardInterrupt:
        print("Program Exit.")
    else:
        if equation.count(OPEN_PARENTHESIS) == equation.count(CLOSING_PARENTHESIS):
            print(calculate(equation))
        else:
            print("Your parenthesis count is uneven. Please change your equation.")

def calculate(equation: str) -> typing.Any:
    return eval(equation) 

if __name__ == "__main__":
    main()
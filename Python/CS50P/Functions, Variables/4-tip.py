# complete the empty functions

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.strip("$"))


def percent_to_float(p):
    return float(p.strip("%"))/100

def test(price,tip):
    price=float(price.strip("$"))
    tip=float(tip.strip("%"))/100
    print(f"Leave ${price*tip:.2f}")

test("$50.00","15%")
test("$100.00","18%")
test("$15.00","25%")

main()
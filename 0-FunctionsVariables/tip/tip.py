def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = float(dollars * percent)
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = float(str(d).removeprefix("$"))
    return d


def percent_to_float(p):
    x = float(str(p).removesuffix("%"))
    p = x * 0.01
    return p


main()

def main():
    x = str.lower(input("give me a greeting"))
    z = x[0:5]
    y = x[0]
    if z == str("hello"):
        print("$0")
    elif y == str("h"):
        print("$20")
    else:
        print("$100")


main()

def main():
    change = a - 50
    a = int(input("insert coin"))
    while a <= 50:
        if a >= 50:
            print("Amount Due" + change)
        else:
            a = int(input("insert coin"))


main()

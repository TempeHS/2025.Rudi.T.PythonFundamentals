def main():
    x = 50

    while x > 0:
        print("Amount Due: ", x)
        y = int(input("Insert Coin: "))
        if y == 5 or y == 10 or y == 25:
            x -= y
    z = abs(x)
    print("change owed: ", z)


main()

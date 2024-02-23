def main():
    a = str(input("enter to get camel cased"))

    for i in a:
        if i.isupper():
            print("_" + i.lower(), end="")
        else:
            print(i, end="")


main()

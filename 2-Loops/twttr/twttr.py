def main():
    a = input("input: ")
    print("output: ", end="")
    for i in a:
        if not i.lower() in ["a", "e", "i", "o", "u"]:
            print(i, end="")
    print()


main()

def main():
    x = str.lower(input("give me the name of a file"))
    gif = x[-1:-5]
    if gif == str(".gif"):
        print("image/gif")
    else:
        print("fail")


main()

def main():
    x = str.lower(
        input("the answer to the Great Question of Life, the Universe and Everything")
    )
    if x == str(42) or x == str("forty two") or x == str("forty-two"):
        print("Yes")
    else:
        print("No")


main()

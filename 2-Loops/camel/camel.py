def main():
    a = str(input("enter to get camel cased"))

    for i in range(len(a)):
        if a[i].isupper():
            j = str(i)
            print(a.replace("j", "_"))


main()
# def uppercase(input_str):
# for i in range(len(input_str)):
# if input_str[i].isupper():
# return input_str[i]
# return "no uppercase characters found"


# print(uppercase(a))

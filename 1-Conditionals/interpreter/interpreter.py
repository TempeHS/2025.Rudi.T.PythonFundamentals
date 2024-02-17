def main():
    Q = str(input("Enter equation here"))
    t = Q.split()

    a = float(t[0])
    b = t[1]
    c = float(t[2])

    if b == "*":
        ans = a * c
        print(ans)
    elif b == "/":
        ans = a / c
        print(ans)
    elif b == "+":
        ans = a + c
        print(ans)
    else:
        ans = a - c
        print(ans)


main()

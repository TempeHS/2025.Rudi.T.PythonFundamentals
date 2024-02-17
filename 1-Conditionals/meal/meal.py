def main():
    x = str(input("what is the time?"))
    stime = x.split(":")
    hour = float(60)
    smin = float(stime[1])
    shour = float(stime[0])
    thour = smin / hour
    time = shour + thour
    brkst = float(7)
    brkfn = float(8)
    lnchst = float(12)
    lnchfn = float(13)
    dnst = float(18)
    dnfn = float(19)
    if time >= brkst and time <= brkfn:
        print("breakfast time")
    elif time >= lnchst and time <= lnchfn:
        print("lunch time")
    elif time >= dnst and time <= dnfn:
        print("dinner time")
    else:
        print("nothing")


main()

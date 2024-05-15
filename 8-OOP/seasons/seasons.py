from datetime import date

from num2words import num2words


def conv_to_int():
    ansa = str(input("what date were you born? (YYYY.MM.DD)\n"))
    if len(ansa) != 10:
        SystemExit
    else:
        split = ansa.split(".")
        todate = str(date.today())
        csplit = todate.split("-")
        YYYY = int(str(csplit[0])) - int(str(split[0]))
        MM = int(str(csplit[1])) - int(str(split[1]))
        DD = int(str(csplit[2])) - int(str(split[2]))

        day = int(1440)
        month = int(43800)
        year = int(525600)

        ymenut = YYYY * year
        mmenut = MM * month
        dmenut = DD * day
        everything = ymenut + mmenut + dmenut
        print(num2words(everything) + str(" minutes"))


conv_to_int()

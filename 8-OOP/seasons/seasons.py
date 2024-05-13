from datetime import date


def conv_to_int():
    ansa = str(input("what date were you born? (YYYY.MM.DD)\n"))
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
    print(everything)

    # time_difference = ans - date.today()


# def conv_to_plain_txt():


# conv_to_int() NUM2WORD

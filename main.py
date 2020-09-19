import datetime


def main():
    menu()


def menu():
    print("Social Security Full Retirement Age Calculator\n")
    try:
        initial_year = int(input("Enter the year of birth or press any key to exit "))
        initial_month = int(input("Enter the month of birth "))

        ret_year, ret_month = year_calculate(initial_year)
        date_month, total_year = month_calculate(initial_year, initial_month, ret_month, ret_year)
        print("your full retirement age is", ret_year, "and", ret_month, "months")
        print("this will be in", date_month, " of ", total_year)
    except ValueError:
        exit()


# Year Calculation
def year_calculate(year):
    ret_year = 65
    ret_month = 0

    if 1900 <= year <= 1937:
        return ret_year, ret_month
    elif 1937 < year < 1943:
        count = year - 1937
        for x in range(count):
            ret_month += 2
        return ret_year, ret_month
    elif 1943 <= year <= 1954:
        ret_year = 66
        ret_month = 0
        return ret_year, ret_month
    elif 1954 < year < 1960:
        ret_year = 66
        count = year - 1954
        for x in range(count):
            ret_month += 2
        return ret_year, ret_month
    elif year >= 1960:
        ret_year = 67
        ret_month = 0
        return ret_year, ret_month
    else:
        print("Invalid year")
        exit()


# Month calculation
def month_calculate(year, month, ret_month, ret_year):
    if 0 < month <= 12:
        total_month = month + ret_month
        total_year = year + ret_year
        if total_month <= 12:
            final_month = datetime.datetime(1990, total_month, 1)
        else:
            total_month -= 12
            total_year += 1
            final_month = datetime.datetime(1990, total_month, 1)
        date_month = final_month.strftime("%B")
        return date_month, total_year
    else:
        print("Invalid month")
        exit()


main()

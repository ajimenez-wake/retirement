import CalculateRetirement as Retire


def main():
    menu()


def menu():
    print("Social Security Full Retirement Age Calculator\n")
    loop_sentry = True
    while loop_sentry:
        try:
            initial_year = int(input("Enter the year of birth or press any key to exit "))
            loop_sentry = False
        except ValueError:
            print("Invalid input.")
    loop_sentry = True
    while loop_sentry:
        try:
            initial_month = int(input("Enter the month of birth "))
            loop_sentry = False
        except ValueError:
            print("Invalid input")

    ret_year, ret_month = Retire.year_calculate(initial_year)
    date_month, total_year = Retire.month_calculate(initial_year, initial_month, ret_month, ret_year)
    print("your full retirement age is", ret_year, "and", ret_month, "months")
    print("this will be in", date_month, " of ", total_year)


main()

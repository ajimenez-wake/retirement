from math import floor


def main():
    menu()


def menu():
    print("Social Security Full Retirement Age Calculator")
    birth_year = input("Enter the year of birth or [E]xit: ")

    # All calculations done in months to simplify math.
    age = int(birth_year) * 12
    if str(birth_year).upper() != "E":
        birth_month = input("Enter the month of birth: ")
        birth_month = int(birth_month)
        age += 12 - birth_month
        retire_age = get_retire_age(age)
        retire_month = retire_age % 12
        retire_year = floor(retire_age / 12)
    print("Your full retirement age is ", retire_year, " and ", retire_month, " months")

    retirement_month = birth_month + retire_month
    retirement_year = int(birth_year) + retire_year
    if retirement_month > 12:
        retirement_month -= 12
        retirement_year += 1
    print("This will be in ", get_month_by_int(retirement_month), retirement_year)


def get_retire_age(age):
    birth_year = floor(age / 12)
    print(birth_year)

    # Birth year 37
    if birth_year <= 1937:
        return 780

    # Birth year 38
    if birth_year == 1938:
        return 782

    # Birth year 39
    if birth_year == 1939:
        return 784

    # Birth year 40
    if birth_year == 1940:
        return 786

    # Birth year 41
    if birth_year == 1941:
        return 788

    # Birth year 42
    if birth_year == 1942:
        return 790

    # Birth year 43 - 54
    if 1943 <= birth_year <= 1954:
        return 792

    # Birth year 55
    if birth_year == 1955:
        return 794

    # Birth year 56
    if birth_year == 1956:
        return 796

    # Birth year 57
    if birth_year == 1957:
        return 798

    # Birth year 58
    if birth_year == 1958:
        return 800

    # Birth year 59
    if birth_year == 1959:
        return 802

    # Birth year > 59
    if birth_year >= 1960:
        return 804


def get_month_by_int(month):
    month -= 1
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months[month]


def get_current_year():
    # Leaves a method to call for future rewrite hardcoded for now.
    return 2020


main()

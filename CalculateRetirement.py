import datetime


# Year Calculation
def year_calculate(year):
    ret_year = 65
    ret_month = 0
    if 1900 <= year <= 1937:
        return ret_year, ret_month
    elif 1937 < year < 1943:
        count = year - 1937
        ret_month = ret_month + (2 * count)
        return ret_year, ret_month
    elif 1943 <= year <= 1954:
        ret_year = 66
        ret_month = 0
        return ret_year, ret_month
    elif 1954 < year < 1960:
        ret_year = 66
        count = year - 1954
        ret_month = ret_month + (2 * count)
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

def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


year = input("ВВедите год в формате ГГГГ: ")
year_result = int(year)

print('год ' + str(year_result) + ': ' + str(is_year_leap(year_result)))

def is_year_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if year < 1582 or not (1 <= month <= 12):
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return 29 if month == 2 and is_year_leap(year) else days[month - 1]

def day_of_year(year, month, day):
    md = days_in_month(year, month)
    if md is None or not (1 <= day <= md):
        return None
    return sum(days_in_month(year, m) for m in range(1, month)) + day

print(day_of_year(2000, 12, 31))  # 366
print(day_of_year(2023, 2, 29))   # None

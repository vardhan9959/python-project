def is_leap_year(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    return True
  else:
    return False
yr = 2024
if is_leap_year(yr):
  print(f"{yr} is a leap year.")
else:
  print(f"{yr} is not a leap year.")
import datetime

given_date = datetime.date(2020, 2, 25)
print("Given Date:")
print(given_date)

days_to_subtract = 7
returned_date = given_date - datetime.timedelta(days=days_to_subtract)
print("New Date:")
print(returned_date)
month = input("Enter a month name: ")

month_dict = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30,
              'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

days = month_dict.get(month.capitalize())

if days:
    print("Number of days in", month, "is", days)
else:
    print("Invalid month name")

import datetime


provided_data = 'Jan 15, 2023 - 12:05:33'

python_date = datetime.datetime.strptime(provided_data, '%b %d, %Y - %H:%M:%S')
print(python_date)


full_month = python_date.strftime('%B')
print(full_month)


new_date_format = python_date.strftime('%d.%m.%Y, %H:%M')
print(new_date_format)

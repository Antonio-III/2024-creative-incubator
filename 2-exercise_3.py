import datetime

current_datetime = datetime.datetime.now()
date_format = "%Y-%m-%d %H:%M:%S"
print(current_datetime.strftime(date_format))
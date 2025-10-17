from datetime import datetime, timedelta

# Get the current date and time
time_now = datetime.now()
current_time = time_now.strftime("%d-%m-%Y")


limit = time_now - timedelta(days=(30 * 365))
selisih = limit.strftime("%d-%m-%Y")

print(selisih)


dateee = "16-10-2023"

# The format code matching the dateee's layout
# %Y for four-digit year, %m for two-digit month, %d for two-digit day
# %H for 24-hour format hour, %M for two-digit minute, %S for two-digit second
format_code = "%d-%m-%Y"

# Convert the string to a datetime object
datetime_object = datetime.strptime(dateee, format_code)

print(datetime_object)
print(type(datetime_object))

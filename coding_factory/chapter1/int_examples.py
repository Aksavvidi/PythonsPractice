# Giving seconds
total_seconds = 105310

# Calculating the number of days
days = total_seconds // (24 * 60 * 60)

# Calculations the remaining seconds (-days)
remaining_seconds = total_seconds - (days * 24 * 60 * 60)

# Calculating the number of hours
hours = remaining_seconds // (60 * 60)

# Calculations the remaining seconds (-days)
remaining_seconds = remaining_seconds - (hours * 60 * 60)

# Calculating the number of minutes
minutes = remaining_seconds // 60

# Calculations the remaining seconds (-days -minutes)
seconds = remaining_seconds - (minutes * 60)

# print days, minutes, seconds
print("days:", days, "hours:", hours, "minutes:", minutes, "seconds:", seconds)

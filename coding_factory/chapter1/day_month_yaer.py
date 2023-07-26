# Αριθμό ημερών -> ..years, ..months, ..days

# Giving total days 
total_days = 8074

# calculate the number of years
years = total_days // 365

# Calculate the remaining number of days (- years)
days_remaining = total_days - (years * 365)

# calculate the number of months
months = days_remaining // 30

# Calculate the remaining number of days (-months)
days = days_remaining - (months * 30)

#Printing the results
print(f"{years} years, {months} months, {days} days")

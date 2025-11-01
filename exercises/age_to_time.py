years = int(input("Enter your age in years: "))

days = years * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"Your age in hours: {hours:,}")
print(f"Your age in minutes: {minutes:,}")
print(f"Your age in seconds: {seconds:,}")
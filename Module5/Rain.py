# Asking user for input
years = int(input("Number of years: "))

# Creating and initializing the variables
totalMonths = 0
totalRain = 0

for year in range(1, years + 1):
    print(f"Year {year}:")
    
    for month in range(1, 13):
        rainFall = float(input(f"Inches of rainfall for month {month}: "))
        totalMonths += rainFall
        totalRain += 1

# Calculate the average
averageRainfall = totalRain / totalMonths

# Displaying the results
print(f"\nTotal number of months: {totalMonths}")
print(f"Total inches of rainfall: {totalRain:.2f}")
print(f"Average rainfall per month: {averageRainfall:.2f} inches")

# Ask user for the number of books
booksPurchased = int(input("Input the number of books: "))

# if statements to determine the number of points
if booksPurchased == 0:
    points = 0
elif booksPurchased == 2:
    points = 5
elif booksPurchased == 4:
    points = 15
elif booksPurchased == 6:
    points = 30
elif booksPurchased >= 8:
    points = 60
else:
    points = 0 
    # Incase of invalid input

print(f"You have earned {points} points")

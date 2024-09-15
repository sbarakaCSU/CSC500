num1 = int(input("Please enter an integer for the first number: "))
while True:
    num2 = int(input("Please enter an integer for the second number: "))
    if num2 != 0:
        break
    else:
        print("The second number cannot be zero")

# Calculating sum
sum = num1 + num2
print ("The sum of the two numbers are: ", sum)

#Calculating difference
difference = num1 - num2
print ("The difference of two numbers are: ", difference)

#Calculating product
product = num1 * num2
print ("The product of two numbers are: ", product)

#Calculating quotient
quotient = num1 // num2
print ("The quotient of two numbers are: ", quotient)
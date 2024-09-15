num1 = float(input("Please enter an integer for the first number: "))
while True:
    num2 = float(input("Please enter an integer for the second number: "))
    if num2 != 0:
        break
    else:
        print("The second number cannot be zero")

#Calculating product
product = num1 * num2
print ("The product of two numbers are: ", product)

#Calculating quotient
quotient = num1 / num2
print ("The quotient of two numbers are: ", quotient)
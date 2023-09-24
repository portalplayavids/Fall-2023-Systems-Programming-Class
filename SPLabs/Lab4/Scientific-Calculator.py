# Elijah Guzman - nze594 - 09/20/2023
# Description: A scientific calculator that can perform basic operations w/ user input.

# Importing math library
import math

def ScientificCalculator():

    # Defining the variables
    num1 = 0
    num2 = 0
    operation = 0
    result = 0

    # Printing the menu
    print("Welcome to the Scientific Calculator!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Logarithm")
    print("11. Quit")

    # Getting the user input
    operation = int(input("Please select an operation: "))
    print()

    # If the user selects addition
    if operation == 1:
        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Please enter the second number: "))
        result = num1 + num2
        print("The result is: ", result)

    # If the user selects subtraction
    elif operation == 2:
        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Please enter the second number: "))
        result = num1 - num2
        print("The result is: ", result)

    # If the user selects multiplication
    elif operation == 3:
        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Please enter the second number: "))
        result = num1 * num2
        print("The result is: ", result)

    # If the user selects division
    elif operation == 4:
        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Please enter the second number: "))
        result = num1 / num2
        print("The result is: ", result)
        
    # If the user selects exponentiation
    elif operation == 5:
        num1 = float(input("Please enter the base: "))
        num2 = float(input("Please enter the exponent: "))
        result = num1 ** num2
        print("The result is: ", result)

    # If the user selects square root
    elif operation == 6:
        num1 = float(input("Please enter the number: "))
        result = math.sqrt(num1)
        print("The result is: %2d ", result)

    # If the user selects sine
    elif operation == 7:
        num1 = float(input("Please enter the number: "))
        result = math.sin(num1)
        print("The result is: ", result)
    
    # If the user selects cosine
    elif operation == 8:
        num1 = float(input("Please enter the number: "))
        result = math.cos(num1)
        print("The result is: ", result)

    # If the user selects tangent
    elif operation == 9:
        num1 = float(input("Please enter the number: "))
        result = math.tan(num1)
        print("The result is: ", result)

    # If the user selects logarithm
    elif operation == 10:
        num1 = float(input("Please enter the number: "))
        result = math.log(num1)
        print("The result is: ", result)

    # If the user selects quit
    elif operation == 11:
        print("Goodbye!")

    # If the user selects an invalid option
    else:
        print("Invalid option!")

#after producing the result, the program will ask the user if they want to continue
#if the user selects yes, the program will run again
#if the user selects no, the program will end and print "Goodbye!"
    print()
    print("Would you like to continue?")
    print("1. Yes")
    print("2. No")
    print()
    operation = int(input("Please select an option: "))
    print()

    if operation == 1:
        ScientificCalculator()
    elif operation == 2:
        print("Goodbye!")
    else:
        print("Invalid option!")

ScientificCalculator()
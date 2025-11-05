# ask the user to enter an operation
print("Select operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# get input from the user
choice = input("Enter choice (1/2/3/4): ")

# get numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# perform the selected operation
if choice == '1':
    print(num1, "+", num2, "=", num1 + num2)

elif choice == '2':
    print(num1, "-", num2, "=", num1 - num2)

elif choice == '3':
    print(num1, "*", num2, "=", num1 * num2)

elif choice == '4':
    if num2 != 0:
        print(num1, "/", num2, "=", num1 / num2)
    else:
        print("Error! Division by zero.")

else:
    print("Invalid input")


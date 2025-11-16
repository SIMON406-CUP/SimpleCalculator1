print("welcome to calculator")

# Ask the user to enter an operation)
print("\n select operation")
print("1: Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5: exit")

# get input from the user
choice = input("Enter choice (1/2/3/4/5): ")

if choice == '5':
    print ("Exiting---")
    exit()

    #Get unlimited numbers
numbers = input("Enter numbers separated by space: ").split()
numbers = [float(num) for num in numbers]

# perform the selected operation
if choice == '1': #Add
    results = num1+num2
    print("the result is:" ,result)

elif choice == '2':
    result = num1 - num2
    print("The result is:", result)

elif choice == '3':
    result = num1 * num2
    print("The result is:", result)

elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("The result is:", result)
    else:
        print("Error! Cannot divide by zero.")

else:
    print("Invalid choice!")
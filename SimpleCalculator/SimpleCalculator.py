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

# Perform operations
if choice == '1':   # Add
    result = sum(numbers)
    print("The result is:", result)

elif choice == '2': # Subtract
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    print("The result is:", result)

elif choice == '3': # Multiply
    result = 1
    for num in numbers:
        result *= num
    print("The result is:", result)

elif choice == '3': # Multiply
    result = 1
    for num in numbers:
        result *= num
    print("The result is:", result)

else:
    print("Invalid choice!")
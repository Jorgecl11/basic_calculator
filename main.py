print("\t****Basic Calculator****")

print("\nPlease enter two numbers")
while True: #outer loop for retry fucntionality
    while True: #Inout validation for numbers
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter a second number: "))
            break
        except ValueError:
            print("Error: Please enter valid numerical values.")

    # operation selection and execution
    while True:
        print("\nChoose an operation:")
        print("1. Addition\n2. Subtraction\n3. Division\n4. Multiplication")
        print("5. Exit")

        # input validation and execution
        try:
            operation = int(input("Enter your choice (1-5)"))
        except ValueError:
            print("Please enter a valid number between 1 and 5 for the operation.")
            continue

        # perform the chosen operation
        if operation ==1:
            result = num1 + num2
            print(f"Addition: {num1} + {num2} = {result}")
        elif operation == 2:
            result = num1 - num2
            print(f"Subtraction: {num1} - {num2} = {result}")
        elif operation == 3:
            if num2 == 0:
                print("Error: Cannot divide by zero!")
            else:
                result = num1 / num2
                print(f"Division: {num1} / {num2} = {result}")
        elif operation == 4:
            result = num1 * num2
            print(f"Multiplication: {num1} * {num2} = {result}")
        elif operation == 5:
            print("Thank you for using the calculator. Goodbye!")
            exit()  # Exit the program
        else:
            print("Error: Invalid choice. Please select a number between 1 and 5.")
            continue

        # Retry prompt
        retry = input("\nWould you like to perform another calculation? (yes/no): ").strip().lower()
        if retry == "yes":
            break  # Restart the outer loop
        elif retry == "no":
            print("Thank you for using the calculator. Goodbye!")
            exit()
        else:
            print("Invalid response. Returning to the main menu.")
            break  # Return to operation selection



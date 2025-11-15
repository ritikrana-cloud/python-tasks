# Define the functions for basic arithmetic operations

def add(n1, n2):
    """Adds two numbers and returns the sum."""
    return n1 + n2

def subtract(n1, n2):
    """Subtracts the second number from the first and returns the difference."""
    return n1 - n2

def multiply(n1, n2):
    """Multiplies two numbers and returns the product."""
    return n1 * n2

def divide(n1, n2):
    """Divides the first number by the second, handling division by zero."""
    if n2 == 0:
        # Return a specific error message if the divisor is zero
        return "Error: Cannot divide by zero"
    return n1 / n2

# Main function to run the calculator logic
def calculator():
    # Start an infinite loop that runs until the 'break' statement is hit
    while True:
        print("\n--- Simple Calculator ---")
        # Print the menu options for the user
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")

        # Use input() to get the user's operation choice
        choice = input("Enter choice (1/2/3/4/5): ")

        # Check if the user chose to exit
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break  # Exit the while loop

        # Check if the choice is a valid operation (1 through 4)
        if choice in ('1', '2', '3', '4'):
            try:
                # Use input() again to get the numbers, converting them to float
                # float() allows for both integers and decimals
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                # Handle non-numeric input gracefully
                print("Invalid input. Please enter numbers only.")
                continue  # Skip the rest of the loop and start over

            result = None
            op_symbol = ''

            # Use if/elif statements to call the correct function
            if choice == '1':
                result = add(num1, num2)
                op_symbol = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                op_symbol = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                op_symbol = '*'
            elif choice == '4':
                result = divide(num1, num2)
                op_symbol = '/'

            # Print the final result in a formatted string
            # Check if the result is an error message (string) or a valid number
            if isinstance(result, str) and result.startswith("Error"):
                 print(result)
            else:
                 # f-string formatting for clear output
                 print(f"{num1} {op_symbol} {num2} = {result}")

        else:
            # Handle invalid choices that are not 1-5
            print("Invalid choice. Please enter a number between 1 and 5.")

# Standard Python entry point: ensures 'calculator()' runs when the script is executed
if __name__ == "__main__":
    calculator()
    
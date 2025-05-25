def get_number_from_input(message:str = "Enter a number: ") -> int:

    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def cli_main():
    print("Welcome to the CLI Calculator")
    
    a = get_number_from_input("Enter the first number: ")
    b = get_number_from_input("Enter the second number: ")
    # TODO: let user choose operation

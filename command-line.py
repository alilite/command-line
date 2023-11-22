import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init(autoreset=True)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def main():
    print(Fore.GREEN + "Simple Calculator" + Style.RESET_ALL)

    while True:
        print("\nChoose operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Quit")

        choice = input("Enter choice (1/2/3): ")

        if choice == '3':
            print("Goodbye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter valid numbers." + Style.RESET_ALL)
            continue

        if choice == '1':
            result = add(num1, num2)
            print(Fore.CYAN + f"Result: {result}" + Style.RESET_ALL)
        elif choice == '2':
            result = subtract(num1, num2)
            print(Fore.CYAN + f"Result: {result}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid choice. Please enter 1, 2, or 3." + Style.RESET_ALL)

if __name__ == "__main__":
    main()

class FactorialCalculator:
    def __init__(self, number):
        self.number = number

    def calculate(self):
        if self.number < 0:
            return None  # Factorial doesn't exist for negative numbers
        elif self.number == 0 or self.number == 1:
            return 1
        else:
            fact = 1
            for i in range(2, self.number + 1):
                fact *= i
            return fact

def main():
    print("Welcome to the Factorial Calculator Project!")
    
    try:
        num = int(input("Enter a non-negative integer: "))
        calculator = FactorialCalculator(num)
        result = calculator.calculate()

        if result is None:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            print(f"The factorial of {num} is: {result}")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()

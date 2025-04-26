# factorial_prime_project.py

class NumberAnalyzer:
    def __init__(self, number):
        self.number = number

    def calculate_factorial(self):
        if self.number < 0:
            return None  # Factorial doesn't exist for negative numbers
        elif self.number == 0 or self.number == 1:
            return 1
        else:
            fact = 1
            for i in range(2, self.number + 1):
                fact *= i
            return fact

    def is_prime(self):
        if self.number <= 1:
            return False
        for i in range(2, int(self.number ** 0.5) + 1):
            if self.number % i == 0:
                return False
        return True

def main():
    print("Welcome to the Number Analyzer Project!")
    
    try:
        num = int(input("Enter a non-negative integer: "))
        analyzer = NumberAnalyzer(num)

        # Factorial Calculation
        factorial_result = analyzer.calculate_factorial()

        if factorial_result is None:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            print(f"The factorial of {num} is: {factorial_result}")

        # Prime Check
        if analyzer.is_prime():
            print(f"{num} is a Prime Number.")
        else:
            print(f"{num} is NOT a Prime Number.")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()

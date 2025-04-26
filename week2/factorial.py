def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n - 1)

# Take user input
num = int(input("Enter a non-negative integer: "))

# Check for valid input
if num < 0:
    print("fac is not defined for negative numbers.")
else:
    result = fac(num)
    print(f"The factorial of {num} is: {result}")

def fibonacci(n):
    """Print Fibonacci numbers up to n."""
    a, b = 0, 1
    print("Fibonacci series up to", n, ":")
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b
    print()


def factorial(n):
    """Return the factorial of n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main():
    n = int(input("Enter a number (N): "))

    if n < 0:
        print("Please enter a non-negative number.")
        return

    fibonacci(n)
    print(f"Factorial of {n} is {factorial(n)}")


if __name__ == "__main__":
    main()
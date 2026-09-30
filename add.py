def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
            # If both numbers are integers, display as int
            if num1.is_integer() and num2.is_integer():
                print(int(add(num1, num2)))
            else:
                print(add(num1, num2))
        except ValueError:
            print("Please provide valid numbers.")
    else:
        print("Usage: python add.py <number1> <number2>")

def convert(fraction):
    while True:
        try:
            a, b = map(int, fraction.split('/'))

            if b == 0:
                raise ZeroDivisionError
            if a > b:
                raise ValueError
        except (ValueError, ZeroDivisionError):
            pass
        else:
            result = round(a / b * 100)  # Convert to percentage and round
            return max(0, min(result, 100))  # Ensure the result is between 0 and 100

def gauge(percentage):
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        return f"{percentage:.0f}%"  # Ensure it returns the percentage string

def main():
    inp = input("Fraction: ")
    g = convert(inp)  # Get the percentage as an integer
    print(gauge(g))  # Print the gauge output based on the percentage

if __name__ == "__main__":
    main()

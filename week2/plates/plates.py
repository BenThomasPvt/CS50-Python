def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check length
    if not (2 <= len(s) <= 6):
        return False

    # Check starts with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Check for invalid characters (only letters and digits)
    if not s.isalnum():
        return False

    # Check if numbers are at the end and do not start with '0'
    num_index = None
    for i, char in enumerate(s):
        if char.isdigit():
            num_index = i
            break

    # If there are numbers, check the conditions
    if num_index is not None:
        # Check if any letters follow numbers
        if any(char.isalpha() for char in s[num_index:]):
            return False
        # Check that the first number is not '0'
        if s[num_index] == '0':
            return False

    return True

if __name__ == "__main__":
    main()

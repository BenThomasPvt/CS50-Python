import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.match(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        return sp(ip)
    else:
        return False


def sp(ip):
    cut = ip.split('.')
    for number in cut:
        # Check if the octet is in the range 0-255
        if int(number) < 0 or int(number) > 255:
            return False
        # Check for leading zeros (valid only for "0")
        if len(number) > 1 and number[0] == '0':
            return False
    return True


if __name__ == "__main__":
    main()

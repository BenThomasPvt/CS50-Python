def main():
    a = input("Greeting: ")
    val = value(a)
    print(f"${val}")


def value(greeting):
    greeting = greeting.strip().lower()
    if 'hello' in greeting:
        return 0
    elif greeting.startswith('h'):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

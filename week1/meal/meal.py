def main():
    a = input("What time is it? ")
    ainh= convert(a)

    if ainh >= 7 and ainh <= 8:
        print("breakfast time")
    elif ainh >= 12 and ainh <= 13:
        print("lunch time")
    elif ainh >= 18 and ainh <= 19:
        print("dinner time")

def convert(time):
    h,m = map(int, time.split(':'))
    return h + m/60


if __name__ == "__main__":
    main()

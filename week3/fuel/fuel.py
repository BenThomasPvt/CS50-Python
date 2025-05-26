while True:
    try:
        a, b = map(int, input("Fraction: ").split('/'))

        if b == 0:
            raise ZeroDivisionError
        if a > b:
            raise ValueError

    except (ValueError, ZeroDivisionError):
        pass

    else:
        break

per =(a/b)*100

if per >= 99:
    print('F')
elif per<= 1:
    print('E')
else:
    print(f"{per:.0f}%")

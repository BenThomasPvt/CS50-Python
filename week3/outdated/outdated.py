months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        if '/' in date:
            m, d, y = map(int, date.split('/'))

        elif ',' in date:
            m_d, y = date.split(',')
            m, d = m_d.split(' ')
            if m in months:
                m = months.index(m) + 1

            m, d, y = map(int, (m, d, y))
        else:
            continue

        if m > 12 or d > 31:
            continue
        break

    except (ValueError, KeyError):
        pass

print(f"{y}-{m:02}-{d:02}")

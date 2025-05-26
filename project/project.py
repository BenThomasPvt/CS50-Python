import os


def get_attendance_data():
    print("Please enter the attendance data line by line (use 'end' to stop):\n")
    # Take multiline input from the user for the attendance data
    str_data = ""
    while True:
        line = input()
        if line.lower() == "end":
            break
        str_data += line + "\n"
    return str_data


def calculate_attendance(str_data):
    present = absent = dash = 0
    plist = []  # List to store present days
    alist = []  # List to store absent days
    hlist = []  # List to store half days

    # Iterate through the data in a single pass
    for line in str_data.splitlines():
        parts = line.split("\t")
        # date = parts[0]  # The first part is the date (e.g., 11/21/2024(Thu))
        attendance = parts[1:]  # The rest are the attendance data

        p_count = attendance.count('P')
        a_count = attendance.count('A')

        # Count based on classes (P, A, -)
        present += p_count
        absent += a_count
        dash += attendance.count('-')

        # Count based on days and store day information
        if p_count > 0 and a_count > 0:
            hlist.append(line)
            continue
        elif p_count > 0:
            plist.append(line)
        elif a_count > 0:
            alist.append(line)

    return present, absent, dash, plist, alist, hlist


def display_attendance(present, absent, dash, plist, alist, hlist):
    total_classes = present + absent + dash
    total_days = len(plist) + len(alist) + len(hlist)
    attendance_classes = (present / (present + absent)) * 100 if present + absent > 0 else 0
    attendance_days = ((len(plist) + len(hlist)) / total_days) * 100 if total_days > 0 else 0

    os.system('clear')

    print(
        f"\t\tCONSIDERING CLASSES :\nPresent classes= {present}\nAbsent classes= {absent}\nNot assigned classes= {dash}\nTotal classes = {total_classes}\nAssigned classes = {present + absent}\nAttendance = {attendance_classes:.2f}%")

    print(
        f"\n\n\t\tCONSIDERING DAYS:\nPresent days = {len(plist)}\nAbsent days = {len(alist)}\nHalf days = {len(hlist)}\nTotal days = {total_days}\nAttendance = {attendance_days:.2f}%\n")

    # Display the lists for present, absent, and half days if they exist
    if plist:
        print(f"\nPresent Days:")
        print("\n".join(plist))

    if alist:
        print(f"\nAbsent Days:")
        print("\n".join(alist))

    if hlist:
        print(f"\nHalf Days:")
        print("\n".join(hlist))


def main():
    # Get the attendance data from user input
    str_data = get_attendance_data()

    # Calculate all attendance data in one pass
    present, absent, dash, plist, alist, hlist = calculate_attendance(str_data)

    # Display the summary
    display_attendance(present, absent, dash, plist, alist, hlist)


if __name__ == "__main__":
    main()

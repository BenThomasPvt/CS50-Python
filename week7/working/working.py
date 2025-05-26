import re


def convert(s):
    # Regular expression to match the 12-hour time format with flexibility in spacing and separator
    time_pattern = r"(\d{1,2}):?(\d{2})? (AM|PM) ?(?:to)? ?(\d{1,2}):?(\d{2})? (AM|PM)"

    # Match the input string using the regular expression
    match = re.match(time_pattern, s.strip())
    if not match:
        raise ValueError("Invalid time format.")

    # Extract the times and periods (AM/PM)
    start_hour = int(match.group(1))
    start_minute = int(match.group(2) or 0)
    start_period = match.group(3)
    end_hour = int(match.group(4))
    end_minute = int(match.group(5) or 0)
    end_period = match.group(6)

    # Validate the times
    if not (0 <= start_hour <= 12 and 0 <= start_minute < 60):
        raise ValueError(f"Invalid start time: {start_hour}:{start_minute}")
    if not (0 <= end_hour <= 12 and 0 <= end_minute < 60):
        raise ValueError(f"Invalid end time: {end_hour}:{end_minute}")

    # Convert the start time to 24-hour format
    start_hour_24 = convert_to_24(start_hour, start_minute, start_period)
    end_hour_24 = convert_to_24(end_hour, end_minute, end_period)

    # Return the result in 24-hour format with zero-padded hours
    return f"{start_hour_24:02}:{start_minute:02} to {end_hour_24:02}:{end_minute:02}"


def convert_to_24(hour, minute, period):
    # Handle the conversion of 12-hour time to 24-hour time
    if period == "AM":
        if hour == 12:
            return 0  # Midnight
        return hour
    elif period == "PM":
        if hour == 12:
            return 12  # Noon
        return hour + 12


def main():
    print(convert(input("Hours: ")))


if __name__ == "__main__":
    main()

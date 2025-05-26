from datetime import date
import sys
import inflect

# Function to calculate age in minutes


def calculate_age_in_minutes(birthdate: str) -> int:
    try:
        # Convert birthdate string to a date object
        birth_date = date.fromisoformat(birthdate)
    except ValueError:
        sys.exit("Invalid date format. Please enter in YYYY-MM-DD format.")

    today = date.today()

    # Check if the birthdate is in the future
    if birth_date > today:
        raise ValueError("Birthdate cannot be in the future.")

    # Calculate the difference in days
    delta = today - birth_date

    # Convert days to minutes
    minutes = delta.days * 24 * 60
    return minutes

# Function to convert minutes to English words


def minutes_to_words(minutes: int) -> str:
    p = inflect.engine()
    # Get the word representation and ensure it has "minutes"
    result = p.number_to_words(minutes).replace(" and ", " ")
    return result.capitalize() + " minutes"  # Convert to lowercase and append 'minutes'


def main():
    # Prompt the user for their birthdate
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ").strip()

    # Calculate the age in minutes
    minutes = calculate_age_in_minutes(birthdate)

    # Convert minutes to words and print the result
    print(f"{minutes_to_words(minutes)}")


if __name__ == "__main__":
    main()

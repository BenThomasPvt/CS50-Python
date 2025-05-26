import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        correct = correct_answer(f"{x} + {y} = ", answer)
        score += correct

    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                print("EEE")  # Invalid level, prompt again
        except ValueError:
            print("EEE")  # Non-integer input, prompt again


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError("Level must be 1, 2, or 3.")
    # Generates non-negative integers with `level` digits
    if level == 1:
        return random.randint(0, 10**level - 1)
    return random.randint(10**(level - 1), 10**level - 1)


def correct_answer(prompt, correct_ans):
    attempts = 0
    while attempts < 3:
        try:
            user_input = int(input(prompt))
            if user_input == correct_ans:
                return 1  # Correct answer
            else:
                print("EEE")
                attempts += 1
        except ValueError:
            print("EEE")
            attempts += 1  # Count this as a failed attempt

    print(f"{prompt}{correct_ans}")  # Show the correct answer after 3 attempts
    return 0


if __name__ == "__main__":
    main()

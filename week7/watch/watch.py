import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Define a regular expression pattern to match YouTube embed URLs
    # We are looking for src="https://www.youtube.com/embed/<video_id>"
    match = re.search(
        r'<iframe[^>]+src="(https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+))"', s)

    if match:
        # Extract the video_id from the second group in the match
        video_id = match.group(2)
        # Return the shorter, shareable URL
        return f"https://youtu.be/{video_id}"
    return None


if __name__ == "__main__":
    main()

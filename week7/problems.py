# problem - 1

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern=r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$"
    if re.search(pattern,ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()

##########################################################################################################################################


# problem - 2

import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"[^>]*></iframe>'
    match = re.search(pattern, s)

    if match:
        return f"https://youtu.be/{match.group(1)}"

    return None


if __name__ == "__main__":
    main()


###########################################################################################################################################

# problem - 3

import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.search(r"^(\d{1,2})(?::([0-5]\d))? (AM|PM) to (\d{1,2})(?::([0-5]\d))? (AM|PM)$", s)
    if not match:
        raise ValueError("Invalid format")

    start_hour, start_min, start_period, end_hour, end_min, end_period = match.groups()

    start = to_24hr(start_hour, start_min, start_period)
    end = to_24hr(end_hour, end_min, end_period)

    return f"{start} to {end}"

def to_24hr(hour, minute, period):
    hour = int(hour)
    minute = int(minute) if minute else 0

    if not (1 <= hour <= 12):
        raise ValueError("Invalid hour")
    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()


##########################################################################################################################################
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

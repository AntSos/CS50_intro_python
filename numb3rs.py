import re
import sys


def main():

    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Pattern for EIPv4 Address
    pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

    # Conditional for r.search() and the given pattern using :=
    if match := re.search(pattern, ip):
        return True

    else:
        return False


if __name__ == "__main__":
    main()

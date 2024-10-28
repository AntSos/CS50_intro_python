import sys
import os


def main():

    # List files in current directory
    file_dir = os.listdir()

    # Check for argv content
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)

    elif len(sys.argv) > 2:
        print("Too many command-line arguments")

    elif len(sys.argv) == 2:
        # Assign argv[1] to a variable
        file = sys.argv[1]
        # Check file parameters
        if file.endswith(".py") != True:
            print("Not a Python file")
            sys.exit(1)

        else:
            if file not in file_dir:
                print("File does not exist")
                sys.exit(1)

            elif file in file_dir:
                # Counter lines
                count_lines = 0
                # Open file
                with open(file) as python_file:
                    # Read each line
                    for line in python_file:
                        # Get rid of spaces
                        strip_line = line.strip()
                        # Avoid counting spaces and comments
                        if len(strip_line) == 0 or strip_line.startswith("#"):
                            None
                        else:
                            # Count line of code
                            count_lines += 1

    print(f"Total lines: {count_lines}")


if __name__ == "__main__":
    main()

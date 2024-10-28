import sys
import os
import pandas as pd
from tabulate import tabulate


# List files in current directory
file_dir = os.listdir()


def main():

    if check_argv() == True:
        # Assign argv[1] to a variable
        file = sys.argv[1]
        # Check file parameters
        if file.endswith(".csv") != True:
            sys.exit("Not a CSV file")

        else:
            if file not in file_dir:
                print("File does not exist")
                sys.exit(1)

            elif file in file_dir:
                # Create a df from file
                df_csv_file = pd.read_csv(file)
                # Print df with tabulate function
                print(
                    tabulate(
                        df_csv_file, showindex=False, headers="keys", tablefmt="grid"
                    )
                )


def check_argv():
    # Check for argv content
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) == 2:
        return True


if __name__ == "__main__":
    main()

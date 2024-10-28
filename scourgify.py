import sys
import os
import csv


# List files in current directory
file_dir = os.listdir()


def main():

    if check_argv() == True:
        # Assign argv[1] to a variable
        in_file = sys.argv[1]
        # Assign argv[2] to a variable
        output_file = sys.argv[2]
        # Check file parameters
        if in_file.endswith(".csv") != True or output_file.endswith(".csv") != True:
            sys.exit("Not a CSV file")

        else:
            if in_file not in file_dir:
                print(f"Could not read {in_file}")
                sys.exit(1)

            elif in_file in file_dir:
                # Open .csv first file and create output file with headers of the first
                with open(in_file, "r") as csv_file, open(
                    output_file, "w"
                ) as output_file:
                    # Read .csv first file as a dictionary
                    reader = csv.DictReader(csv_file)
                    # Wrtite second file as a dictionary
                    writer = csv.DictWriter(
                        output_file, fieldnames=["first", "last", "house"]
                    )
                    # Write headers in output_file
                    writer.writeheader()

                    for row in reader:
                        # Get rid of sapces and split the current name
                        l_name, f_name = row["name"].split(", ")
                        # Write output_file with the newname and current house
                        writer.writerow(
                            {"first": f_name, "last": l_name, "house": row["house"]}
                        )


def check_argv():
    # Check for argv content
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) == 3:
        return True


if __name__ == "__main__":
    main()

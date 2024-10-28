import sys
from PIL import Image, ImageOps


def main():
    # Allowed file extesions
    file_e = (".jpg", ".jepg", ".png")
    # Assig variables to files
    in_file = sys.argv[1].lower()
    out_file = sys.argv[2].lower()
    # Get their name and extension using split
    name_in_file, ext_in_file = in_file.split(".")
    name_out_file, ext_out_file = out_file.split(".")

    # Check file parameters
    try:
        if check_argv() == True:
            # Check end of both files
            if in_file.endswith(file_e) != True or out_file.endswith(file_e) != True:
                sys.exit("Invalid input")
            # Check that both files have the same ending format
            elif ext_in_file != ext_out_file:
                sys.exit("Input and output have different extensions")

    except FileNotFoundError:
        sys.exit("Inputs does not exist")

    # Open images
    try:
        in_photo = Image.open(in_file)
        d_shirt_photo = Image.open("shirt.png")

    except FileNotFoundError:
        sys.exit("Inputs does not exist")

    # Get size of the shirt picture
    d_shirt_size = d_shirt_photo.size
    # Change input image size
    c_in_photo = ImageOps.fit(in_photo, d_shirt_size)
    # Paste image
    c_in_photo.paste(d_shirt_photo, d_shirt_photo)
    # Save file with pasted photo
    c_in_photo.save(out_file)


# Check for argv content
def check_argv():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) == 3:
        return True


if __name__ == "__main__":
    main()

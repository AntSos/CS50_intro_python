def main():

    file_name = input("File name: ").lower().replace(" ", "")

    if file_name.endswith(".jpg"):
        print("image/jpeg")

    elif file_name.endswith(".jpeg"):
        print("image/jpeg")

    elif file_name.endswith(".png"):
        print("image/png")

    elif file_name.endswith(".gif"):
        print("image/gif")

    elif file_name.endswith(".pdf"):
        print("application/pdf")

    elif file_name.endswith(".txt"):
        print("text/plain")

    elif file_name.endswith(".zip"):
        print("application/zip")

    elif file_name.endswith(".bin"):
        print("application/octet-stream")

    else:
        print("application/octet-stream")



if __name__=="__main__":
    main()

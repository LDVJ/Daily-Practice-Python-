try:
    file_size = float(input("Enter File Size (MB): ").strip())
    file_format = input("Enter File Format: .").lower()

    if not file_size < 0:
        if file_size <= 5:
            if file_format == "jpg" or file_format == "png" or file_format == "gif":
                print("Upload successful")
            else:
                print("Invalid format")
        else:
            print("File too large")
    else:
        print("Invalid")

except ValueError:
    print("Invalid Value")
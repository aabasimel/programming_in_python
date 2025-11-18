
while True:
    fname= input("Enter a file name: ")
    try:
        with open(fname, "r") as f:
            print(f.read())
            break
    except FileNotFoundError:
        print(f"Error: The file {fname} was not found.")
    except Exception as e:
        print(f"Error: {e}")
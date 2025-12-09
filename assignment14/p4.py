def main():
    input_filename = input("Enter the input filename: ")

    try:
        with open(input_filename, 'r') as infile:
            content = infile.read().strip()
            numbers = content.split()

            if len(numbers) != 2:
                print("Error: The file must contain exactly two integers.")
                return

            a, b = map(int, numbers)

        
        try:
            result = a / b
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            return

        with open("division.txt", 'w') as outfile:
            outfile.write(str(result))

        print("Result written to division.txt successfully.")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except IOError:
        print(f"Error: Cannot open or write to file.")

if __name__ == "__main__":
    main()

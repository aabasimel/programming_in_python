from mod_conversion import in2cm_table_html

# Read input parameters
start = float(input("Enter start length in inches: "))
end = float(input("Enter end length in inches: "))
step = float(input("Enter step size in inches: "))

# Read choice for output
choice = input("Enter 's' to print on screen or any other key to save to in2cm.html: ").lower()

# Generate HTML table
html_table = in2cm_table_html(start, end, step)

# Output based on choice
if choice == 's':
    print(html_table)
else:
    with open("in2cm.html", "w") as file:
        file.write(html_table)
    print("HTML table saved to in2cm.html")

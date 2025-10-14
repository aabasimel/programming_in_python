



import os

# Your info
first_name = "Ahmed"
last_name = "Abasimel"
email = "myemail@constructor.university"

# Folder containing Python files
folder = "./"  # current folder, change if needed

# List all .py files in folder
py_files = [f for f in os.listdir(folder) if f.endswith(".py")]

# Loop through each Python file
for i, file_name in enumerate(py_files, start=1):
    # Construct header
    header = f"""# CTMS-14
# a4 p{i+1}.py
# {first_name} {last_name}
# {email}

"""
    # Read the original content
    with open(file_name, "r", encoding="utf-8") as f:
        content = f.read()

    # Write the header + original content
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(header + content)

    print(f"Header added to {file_name} as p{i}.py")

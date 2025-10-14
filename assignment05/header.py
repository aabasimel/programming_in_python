import os

# Your info
first_name = "Ahmed"
last_name = "Abasimel"
email = "aabasimel@constructor.university"

# Folder containing Python files - use absolute path to be sure
folder = os.getcwd()  # Get current working directory
print(f"Current working directory: {folder}")

# List all .py files in folder
py_files = [f for f in os.listdir(folder) if f.endswith(".py") and f != "header.py"]
print(f"Python files found: {py_files}")

if not py_files:
    print("No Python files found (excluding header.py)")
else:
    # Loop through each Python file
    for i, file_name in enumerate(py_files, start=1):
        print(f"Processing {file_name}...")
        
        # Construct header
        header_text = f"""# CTMS-14
# a4 p{i}.py
# {first_name} {last_name}
# {email}

"""
        try:
            # Read the original content
            with open(file_name, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Check if header already exists (to avoid duplicates)
            if content.startswith("# CTMS-14"):
                print(f"  Header already exists in {file_name}, skipping...")
                continue
            
            # Write the header + original content
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(header_text + content)
            
            print(f"  ✓ Header added to {file_name} as p{i}.py")
            
        except Exception as e:
            print(f"  ✗ Error processing {file_name}: {e}")
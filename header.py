import os

# Your info
first_name = "Ahmed"
last_name = "Abasimel"
email = "aabasimel@constructor.university"

# Current folder
folder = os.getcwd()
print(f"Current working directory: {folder}")

# Loop through numbered subfolders
i = 1
while True:
    subfolder = os.path.join(folder, f"p{i}")
    file_path = os.path.join(subfolder, f"p{i}.py")
    
    if not os.path.exists(file_path):
        break  # Stop when no more numbered folders/files
    
    print(f"Processing {file_path}...")
    
    # Construct header
    header_text = f"""# CTMS-14
# a4 p{i}.py
# {first_name} {last_name}
# {email}

"""
    try:
        # Read the original content
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Check if header already exists
        if content.startswith("# CTMS-14"):
            print(f"  Header already exists in {file_path}, skipping...")
        else:
            # Write the header + original content
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(header_text + content)
            print(f"  ✓ Header added to {file_path}")
    
    except Exception as e:
        print(f"  ✗ Error processing {file_path}: {e}")
    
    i += 1

example_dict = {
    "apple": 5,
    "banana": 3,
    "orange": 7,
    "grape": 2
}

key_to_check = input("Enter a key to check: ")

if key_to_check in example_dict:
    print(f"The key '{key_to_check}' is present in the dictionary.")
else:
    print(f"The key '{key_to_check}' is NOT present in the dictionary.")

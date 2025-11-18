
def demonstrate_exceptions():
    """Demonstartes how to handle three built-in exceptions."""
    print( "1. ZeroDivisionError Demonstration")
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        result = numerator / denominator
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print(f"{numerator} / {denominator} = {result}")


    print( "2. AttributeError Demonstration")
    try:
        class SimpleClass:
            def __init__(self):
                self.existing_attribute = "I exist!"
        obj = SimpleClass()
        print(obj.existing_attribute)

        # Attempt to access a non-existent attribute
        print (obj.non_existent_attribute) # This will raise an AttributeError
    except AttributeError as e:
        print(f"caught an attribute error: {e}")
    except AttributeError as e:
        print(f"An attribute error occurred: {e}")


    print( "3. IndexError Demonstration")
    try:
        my_list = [1, 2, 3]
        print(my_list[3]) # This will raise an IndexError
    except IndexError as e:
        print(f"An index error occurred: {e}")


if __name__ == "__main__":
    demonstrate_exceptions()
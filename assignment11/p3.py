
class FormulaError(Exception):
    """Custom exception class for formula errors."""
    pass

def simple_calculator():
    print("Enter formula in the format: 'number operator number'")

    while True:
        try:
            user_input = input ("Enter a formula: ").strip()

            if user_input.lower() == 'quit':
                print ("Goodbye!")
                break
            parts = user_input.split()

            if len(parts) != 3:
                raise FormulaError (f"Invalid input format. Expected 3 elements but got {len(parts)}. Format should be: 'number operator number'")
            
            first, operator, second = parts

            try:
                first = float(first)
            except ValueError:
                raise FormulaError ("Invalid input format. The first element should be a number.")

            try:
                second = float(second)
            except ValueError:
                raise FormulaError ("Invalid input format. The third element should be a number.")

            if operator not in ['+', '-', '*', '/']:
                raise FormulaError ("Invalid input format. The second element should be a valid operator (+, -, *, /).")

            if operator == '+':
                result = first + second
            elif operator == '-':
                result = first - second
            elif operator == '*':
                result = first * second
            elif operator == '/':
                if second == 0:
                    raise FormulaError ("Division by zero is not allowed.")
                result = first / second

            print(f"Result: {first} {operator} {second} = {result}")

        except FormulaError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    simple_calculator()

            
     
   
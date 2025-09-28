# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return None  #main.py can detect and print a message
        return num1 / num2
    else:
        return None

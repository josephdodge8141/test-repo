class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2) -> float:
        from operations.addition import add
        return add(num1, num2)

    def subtract(self, num1, num2) -> float:
        from operations.subtraction import subtract
        return subtract(num1, num2)

    def multiply(self, num1, num2) -> float:
        from operations.multiplication import multiply
        return multiply(num1, num2)

    def divide(self, num1, num2) -> float:
        from operations.division import divide
        from utils.error_handler import handle_error

        try:
            return divide(num1, num2)
        except ZeroDivisionError:
            handle_error("Division by zero is not allowed")

    def perform_operation(self):
        from utils.input_handler import get_numeric_input
        from utils.error_handler import handle_error

        operation = input("Enter operation (add/subtract/multiply/divide): ")
        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            handle_error("Invalid operation")
            return

        num1 = get_numeric_input("Enter first number: ")
        num2 = get_numeric_input("Enter second number: ")

        if operation == 'add':
            result = self.add(num1, num2)
        elif operation == 'subtract':
            result = self.subtract(num1, num2)
        elif operation == 'multiply':
            result = self.multiply(num1, num2)
        else:
            result = self.divide(num1, num2)

        print("Result: ", result)
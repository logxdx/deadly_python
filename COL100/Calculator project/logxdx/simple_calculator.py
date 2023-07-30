from stack import Stack

class SimpleCalculator:
    
    def __init__(self):
        self.history = Stack()



    def evaluate_expression(self, input_expressan):
        """
        Evaluates a given expression and returns the result.

        Args:
        - input_expression (str): the expression to evaluate

        Returns:
        - Union[str, float]: the result of the evaluation, or an "Error" string if the input is invalid
        """

        input_expression = Stack()
        token=""

                                                                                        # Tokenize the Input Expression
        for char in input_expressan:
            if char.isdigit():
                token += char
        
            if char == ' ':
                if token!="":
                    input_expression.push(int(token))
                    token=""
        
            elif char in ["+", "-", "*", "/", "(", ")"]:
                if token != "":
                    input_expression.push(int(token))
                    token = ""
                input_expression.push(char)

        if token != "":
            input_expression.push(int(token))

                                                                                        # Check Expression Length
        if len(input_expression.list_items()) != 3:
            self.history.push((input_expressan, "Error"))
            return "Error"

        operator = input_expression.list_items()[1]                                     # Get the Operator
        operands = [input_expression.list_items()[0],input_expression.list_items()[2]]  # Get Operands

        if len(operands) != 2:                                                          # Check for correct number of operands
            self.history.push((input_expressan, "Error"))
            return "Error"

                                                                                        # Convert Operands to Integers
        try:
            operand1 = int(operands[0])
            operand2 = int(operands[1])
        except ValueError:
            self.history.push((input_expressan, "Error"))
            return "Error"

                                                                                        # Evaluate Expression
        if operator == "+":
            result = operand1 + operand2
        elif operator == "-":
            result = operand1 - operand2
        elif operator == "*":
            result = operand1 * operand2
        elif operator == "/":
            if operand2 == 0:                                                           # Check for division by zero
                    self.history.push((input_expressan, "Error"))
                    return "Error"
            result = operand1 / operand2
        else:
            self.history.push((input_expressan, "Error"))
            return "Error"

        result = float(result)                                                          # Convert result to float
        self.history.push((input_expressan, result))
        return result



    def get_history(self):
        return self.history.list_items()

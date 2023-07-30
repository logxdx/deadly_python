from simple_calculator import SimpleCalculator
from stack import Stack

class AdvancedCalculator(SimpleCalculator):
    
    def __init__(self):
        super().__init__()
        self.history = []



    def evaluate_expression(self, input_expression):

                                                                                    # Tokenize the input expression
        tokens = self.tokenize(input_expression)

                                                                                    # Check if brackets are valid
        if not self.check_brackets(tokens):
            self.history.append((input_expression, "Error"))
            return "Error"

                                                                                    # Evaluate the list of tokens
        result = self.evaluate_list_tokens(tokens)

                                                                                    # Update history
        self.history.append((input_expression, result))
        return result



    def tokenize(self, input_expression):
        """
            Tokenizes a given expression into a list of tokens consisting of numbers and arithmetic operators.
        
            :param input_expression: A string representation of the input expression.
            :return: A list of tokens consisting of integers and arithmetic operators.
        """

        tokens = []
        token = ""

        for char in input_expression:
            
            if char.isdigit():
                token += char
            
            if char == ' ':
                if token!="":
                    tokens.append(int(token))
                    token=""
            
            elif char in ["+", "-", "*", "/", "(", ")", "{", "}"]:
            
                if token != "":
                    tokens.append(int(token))
                    token = ""
            
                tokens.append(char)

        if token != "":
            tokens.append(int(token))

        return tokens



    def check_brackets(self, list_tokens):
        """
            Check if the given list of tokens has balanced brackets.
            
            :param list_tokens: A list of strings containing the tokens to be checked.
            :type list_tokens: List[str]
            :return: True if the brackets are balanced, False otherwise.
            :rtype: bool
        """
                
        stack = Stack()

        for token in list_tokens:
      
            if token in ["(", "{"]:
                if token=='{':
                    if '(' in stack.list_items():
                        return False
                stack.push(token)
        
            elif token in [")", "}"]:
                if stack.is_empty():
                    return False

                top = stack.peek()
        
                if (top == "(" and token == ")") or (top == "{" and token == "}"):
                    stack.pop()
        
                else:
                    return False

        return stack.is_empty()



    def evaluate_list_tokens(self, list_tokens):
        """
            Evaluates the given list of tokens.

            :param list_tokens: A list of strings containing the tokens to be evaluated.
            :type list_tokens: List[str]
            :return: The result of the evaluation.
            :rtype: str/float || "Error" OR the result of evaluation
        """

        operand_stack = Stack()
        operator_stack = Stack()

                                                                                     # Define Operator Precedence
        precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2
                     }

                                                                                    # Check for empty brackets in tokenized expression
        for i in range(len(list_tokens)):
            if list_tokens[i]=='(' and list_tokens[i+1]==')':
                return "Error"
            if list_tokens[i]=='{' and list_tokens[i+1]=='}':
                return "Error"
            
                                                                                    # Iterate through each token in the list
        for token in list_tokens:      
            
                                                                                    # Check if token is an Operand
            if isinstance(token, int):
                # Push operand onto the stack
                operand_stack.push(token)


                                                                                    # Check if token is an Operator
            elif token in ["+", "-", "*", "/"]:

                                                                                    # Operator before number in expression : Return "Error
                if operand_stack.is_empty():
                    return "Error"
                
                                                                                    # Evaluate Operators and Operands based on precedence
                while (not operator_stack.is_empty()) and (operator_stack.peek() in ["+", "-", "*", "/"]) and (precedence[operator_stack.peek()] >= precedence[token]) :
                    operator = operator_stack.pop()
                    operand2 = operand_stack.pop()
                    operand1 = operand_stack.pop()

                    result = self.perform_operation(operand1, operand2, operator)
                    if result == "Error":
                        return "Error"
                    operand_stack.push(result)

                                                                                    # Push operator if operator stack is empty OR top element is an operand/bracket OR precedence of present operator < operator at top
                operator_stack.push(token)
                

                                                                                    # Push opening bracket onto operator stack
            elif token in ["(", "{"]:

                                                                                    # Check for invalid bracket combinations                
                if token=='{':
                    if '(' in operator_stack.list_items():
                        return "Error"
                operator_stack.push(token)


                                                                                    # Evaluate Bracketed Expression
            elif token in [")", "}"]:
            
                while not operator_stack.is_empty() and operator_stack.peek() not in ["(", "{"]:
                    operator = operator_stack.pop()
                    operand2 = operand_stack.pop()
                    operand1 = operand_stack.pop()
                    result = self.perform_operation(operand1, operand2, operator)
            
                    if result == "Error":
                        return "Error"
                    operand_stack.push(result)
            
                if not operator_stack.is_empty() and operator_stack.peek() in ["(", "{"]:
                    operator_stack.pop()


                                                                                    # Evaluate remaining operators and operands
        while not operator_stack.is_empty():
            operator = operator_stack.pop()
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()

            result = self.perform_operation(operand1, operand2, operator)
            if result == "Error":
                return "Error"
            
                                                                                    # Check for cases with missing operators
                                                                                    # Handling '2 3 + 3' type cases
            if not operand_stack.is_empty() and  operator_stack.is_empty() :
                return "Error"
            operand_stack.push(result)
        
                                                                                    # Return the final result
        return operand_stack.pop()



    def perform_operation(self, operand1, operand2, operator):
        """
            Performs a mathematical operation given two operands and an operator.
            
            Args:
            - operand1: a numeric value for the first operand.
            - operand2: a numeric value for the second operand.
            - operator: a string value representing the operator to be used in the operation. 
            Must be one of "+", "-", "*", or "/".
            
            Returns:
            - The result of the mathematical operation as a numeric value if the operation is successful.
            - "Error" as a string value if the operation is unsuccessful (e.g. division by zero).
        """

        try :
            if operator == "+":
                return float(operand1 + operand2)
            elif operator == "-":
                return float(operand1 - operand2)
            elif operator == "*":
                return float(operand1 * operand2)
            elif operator == "/":
                if operand2 == 0:
                    return "Error"
                return float(operand1 / operand2)
        except:
             return "Error"



    def get_history(self):
        return self.history

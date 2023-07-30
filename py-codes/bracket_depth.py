def correct_depth(tokens):
    stack = []
    depth = 0

    for token in tokens:
        if token == '(':
            stack.append('(')
            depth += 1
        elif token == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
            depth -= 1
        elif token.isdigit():
            if int(token) != depth:
                return False
        else:
            return False

    return len(stack) == 0

# Example usage:
tokens = ['(', '(', '2', ')', '1', '(', '(', '3', ')', ')', ')', '(', '1', ')', '(', '(', '(', '3', ')', ')', ')']
print(correct_depth(tokens))  # Output: True

tokens = ['(', '(', '2', ')', '1', '(', '(', '3', ')', ')', '(', '1', ')', '(', '(', '(', '3', ')', ')']
print(correct_depth(tokens))  # Output: False

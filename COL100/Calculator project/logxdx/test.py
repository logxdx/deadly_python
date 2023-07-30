from simple_calculator import SimpleCalculator
from advanced_calculator import AdvancedCalculator


expr= "+ 2 3"
calculator = AdvancedCalculator()
answer = calculator.evaluate_expression(expr) # answer should be 2.75
print("Answer:",answer)
tokens = calculator.tokenize(expr)
print("Tokens:",tokens)
answer = calculator.evaluate_list_tokens(tokens)
print("Evaluated Tokens:",answer)
correct_brackets = calculator.check_brackets(tokens) # should be False
print("Brackets",correct_brackets)
history = calculator.get_history()
print(history)
print()

expr= "2 3 + 5"
calculator = AdvancedCalculator()
answer = calculator.evaluate_expression(expr) # answer should be 2.75
print("Answer:",answer)
tokens = calculator.tokenize(expr)
print("Tokens:",tokens)
answer = calculator.evaluate_list_tokens(tokens)
print("Evaluated Tokens:",answer)
correct_brackets = calculator.check_brackets(tokens) # should be False
print("Brackets:",correct_brackets)
history = calculator.get_history()
print(history)

from simple_calculator import SimpleCalculator
from advanced_calculator import AdvancedCalculator
'''
calculator = SimpleCalculator()
answer = calculator.evaluate_expression("2 + 3")
print(answer)  # Output: 5.0
answer = calculator.evaluate_expression("2 +")
print(answer)  # Output: Error
history = calculator.get_history()
print(history)  # Output: [('2 + 3', 5.0), ('2 +', 'Error')]
print("-----------------------")

calculator = AdvancedCalculator()
answer = calculator.evaluate_expression("2 + (3 4)") # answer should be 2.75
print(answer)
answer = calculator.evaluate_expression("2 3 + 3") # answer should be "Error"
print(answer)
tokens = calculator.tokenize("2 + 3") # tokens should be [2, '+', 3]
print(tokens)
answer = calculator.evaluate_list_tokens(tokens) # answer should be 5.0
print(answer)
correct_brackets = calculator.check_brackets(['(', 2, '*',')']) # should be False
print(correct_brackets)
history = calculator.get_history() # history should be [("2 +", "Error"), ("2 + (3 /4)", 2.75)]
print(history)
print("-----------------------")
'''


axpresan = [
            "* 2 3",
            '* 23',
            '2 *3+ 3',
            '3+',
            '+-1',
            '2+3',
            '(2+3)' ,
            '{2+3}',
            '{(2+3)}',
            '({2+3})'
            ,'2()+3/4', 
            "2 + (3 4)", 
            '()', 
            '{}', 
            '({})', 
            '{()}',
            "2+()+3",
            "2++3",
            "2()3",
            "({2+3})",
            "(2+)+3",
            "(2+)3",
            "2+3*{2+3-5}*(6+7*8)-9",
            "(2)+3",
            "2()+3",
            "+3",
            "2+++3",
            "3(+)",
            "A+B",
            "A+(B)",
            "2+(B)3",
            "{5*(56+(68-11)/88)}",
            "2+5*7/8"
            ]

calculator=AdvancedCalculator()
for expr in axpresan:
    answer = calculator.evaluate_expression(expr)
    tokens = calculator.tokenize(expr)
    print("Tokens:",tokens)
    correct_brackets = calculator.check_brackets(tokens)
    print("Bracket Check :",correct_brackets)
    print("Result :",answer)
    print("---------------------------------------------------")

for i in calculator.get_history():
    print(i)
    
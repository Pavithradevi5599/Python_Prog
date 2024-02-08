def are_parentheses_balanced(input_string):
    stack = []
    opening_brackets = {'(', '{', '['}
    closing_brackets = {')', '}', ']'}
    matching_brackets = {'(': ')', '{': '}', '[': ']'}
    
    for char in input_string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            last_opening_bracket = stack.pop()
            if matching_brackets[last_opening_bracket] != char:
                return False
    
    return len(stack) == 0

while True:
    user_input = input("Enter only pairs of parentheses: ")
    
    if are_parentheses_balanced(user_input):
        if all(char in '(){}[]' for char in user_input):
            print("Your entered parantheses: ",user_input)
            break
        else:
            print("Invalid input. Please enter only pairs of parentheses.")

# src/rpn.py
from typing import List, Union

def eval_rpn(tokens: List[str]) -> int:
    """
    Evaluates an arithmetic expression in Reverse Polish Notation (RPN).

    The result of division must be truncated toward zero.
    Example: -7 / 3 = -2
    
    Args:
        tokens: A list of strings representing the RPN tokens (numbers and operators).

    Returns:
        The integer result of the RPN expression.
    """
    stack: List[int] = []
    
    # Set of supported operators
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token not in operators:
            # Token is a number (integer), push it onto the stack
            stack.append(int(token))
        else:
            # Token is an operator. Pop the two top operands (b then a).
            if len(stack) < 2:
                # Should not happen with valid RPN, but good practice
                raise ValueError("Invalid RPN expression: not enough operands.")
                
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = 0

            # Perform the operation
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                # Crucial: Perform integer truncation toward zero.
                # Python's default '//' is floor division (towards negative infinity).
                # The correct method for truncation toward zero is to cast the result 
                # of true division to an integer.
                
                # Check for division by zero
                if operand2 == 0:
                    raise ZeroDivisionError("Division by zero in RPN expression.")

                # Calculate true division
                true_division = operand1 / operand2
                
                # Truncate toward zero: cast the float to int.
                # For positive numbers, this is floor. For negative numbers, this is ceil.
                result = int(true_division)

            stack.append(result)

    # After processing all tokens, the stack must contain the final result
    if len(stack) != 1:
        raise ValueError("Invalid RPN expression: too many operands remaining.")
        
    return stack[0]
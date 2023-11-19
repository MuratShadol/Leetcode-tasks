"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

"""

def evalRPN(tokens):
    result = []
    for i, num in enumerate(tokens):
        if num == "*":
            result.append(result.pop() * result.pop())
        elif num == "-":
            val1, val2 = result.pop(), result.pop()
            result.append(val2 - val1)
        elif num == "+":
            result.append(result.pop() + result.pop())
        elif num == "/":
            val1, val2 = result.pop(), result.pop()
            result.append(int(val2/val1))
        else:
            result.append(int(num))

    return result[0]


number = evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(number)

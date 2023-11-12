"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""

def isValid(s):
    stack = []
    brackets = {"}":"{", ")": "(", "]":"["}
    for sym in range(len(s)):
        if s[sym] in brackets and stack:
            if stack[-1] == brackets[s[sym]]:
                stack.pop()
            else:
                return False
        else:
            stack.append(s[sym])
    return not stack


assert isValid(")") == False
assert isValid("{(()[])}") == True
assert isValid("[][()}]") == False
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

"""

def isPalindrome(s):    
    s = ''.join(letter.lower() for letter in s if letter.isalnum())
    if not s:
        return True
    first = 0
    last = len(s) - 1

    while first <= last:
        if s[first] != s[last]:
            return False
        else:
            first += 1
            last -= 1
    return True 


assert isPalindrome(s = "A man, a plan, a canal: Panama") == True
assert isPalindrome("race a car") == False
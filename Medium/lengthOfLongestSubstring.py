"""
Given a string s, find the length of the longest substring
without repeating characters.

"""

def lengthOfLongestSubstring(s):
    letters = {}
    length = 0
    current_length = 0
    for i in range(len(s)):
        if letters.get(s[i]):
            if current_length > length:
                length = current_length
            current_length = 0
            letters = {}

        letters[s[i]] = True
        current_length += 1
    if current_length > length:
        length = current_length
    if s == "":
        return 0
    elif len(s) == 1:
        return 1
    else:
        return length

print(lengthOfLongestSubstring("dvdf"))
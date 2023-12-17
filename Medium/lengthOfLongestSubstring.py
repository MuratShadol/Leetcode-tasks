"""
Given a string s, find the length of the longest substring
without repeating characters.

"""

def lengthOfLongestSubstring(s):
    chs = set()
    start = 0
    end = 0
    max_ch = 0
    while end < len(s):
        while s[end] in chs:
            chs.remove(s[start])
            start += 1
        chs.add(s[end])
        max_ch = max(end-start+1, max_ch)
        end += 1
    return max_ch


assert lengthOfLongestSubstring("dvdf") == 3
assert lengthOfLongestSubstring("abcabcbb") == 3
assert lengthOfLongestSubstring("pwwkew") == 3
assert lengthOfLongestSubstring("bbbbb") == 1

"""
Пройтись по строке, на каждом шаге запускать цикл,
который будет убирать из сета все вхождения текущего элемента в сет слева.
После цикла добавить элемент в сет, вычислить максимум между текущим значением
окна (подстроки) и существующим.
"""
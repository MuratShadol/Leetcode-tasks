"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

"""

def isAnagram(s, t):
    if len(s) != len(t) or set(s) != set(t):
        return False
    

    shash = {}
    thash = {}

    for i in range(len(s)):
        shash[s[i]] = shash.setdefault(s[i], 0) + 1
        thash[t[i]] = thash.setdefault(t[i], 0) + 1
    return shash == thash


def isAna(s, t):
    if len(s) != len(t):
        return False
    frequency = {}

    for i in range(len(s)):
        frequency[s[i]] = frequency.setdefault(s[i], 0) + 1

    for i in range(len(t)):
        if t[i] not in frequency:
            return False
        
        frequency[t[i]] = frequency.get(t[i]) - 1
        if frequency.get(t[i]) == 0:
            del frequency[t[i]]
    return True

2
assert isAnagram("a", "b") == False
assert isAnagram("ll", "jjj") == False
assert isAnagram("aacc", "ccac") == False
assert isAnagram("lakfr", "alkrf") == True

assert isAna("a", "b") == False
assert isAna("ll", "jjj") == False
assert isAna("aacc", "ccac") == False
assert isAna("lakfr", "alkrf") == True
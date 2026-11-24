# Incorrect attempt, passed the test but logically flawed.
class Solution(object):
    def isAnagram(self, s, t):
        seen = set()
        word = s
        compare = t
        for letter in word:
            seen.add(letter)
        for letter in compare:
            if letter not in seen:
                return False
        return True

# Runtime: 14 ms
class Solution(object):
    def isAnagram(self, s, t):
        seen = {}
        if len(s) != len(t):
            return False
            
        for letter in s:
            if letter in seen:
                seen[letter] += 1
            else:
                seen[letter] = 1

        for letter in t:
            if letter not in seen:
                return False
            else:
                if seen[letter] <= 0:
                    return False
                seen[letter] -= 1
        return True

"""
Input
s = "anagram"
t = "nagaram"

Output = true
Expected = true
"""

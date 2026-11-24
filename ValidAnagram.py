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

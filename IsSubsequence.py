# Runtime: 2 ms
class Solution(object):
    def isSubsequence(self, s, t):
        subs = 0
        orig = 0
        while subs < len(s) and orig < len(t):
            if s[subs] == t[orig]:
                subs += 1
            orig += 1     
        return subs == len(s)

"""
Input
s = "axc"
t = "ahbgdc"

Output = false
Expected = false
"""

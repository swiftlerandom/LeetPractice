# Runtime: 17 ms
class Solution(object):
    def groupAnagrams(self, strs):
        seen = {}

        for word in strs:
            signature = "".join(sorted(word))

            if signature in seen:
                seen[signature].append(word)
            else:
                seen[signature] = [word]

        return list(seen.values())

""" Any order allowed
Input
strs = ["eat","tea","tan","ate","nat","bat"]

Output = [["tan","nat"],["bat"],["eat","tea","ate"]]
Expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

# Runtime: 45ms
class Solution(object):
    def containsDuplicate(self, nums):
        seen = {}
        for i in range(len(nums)):
            num = nums[i]

            if num in seen:
                return True
            seen[num] = i 
        return False

# Runtime: 36ms
class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False

"""
Input
nums = [1,2,3,1]

Output = true
Expected = true
"""

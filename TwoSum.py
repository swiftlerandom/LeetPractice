class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


"""
Input
nums = [2,7,11,15]
target = 9

Output = [0,1]
Expected = [0,1]
"""



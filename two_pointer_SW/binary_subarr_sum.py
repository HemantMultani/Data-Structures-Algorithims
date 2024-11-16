"""
Problem Link:
https://leetcode.com/problems/binary-subarrays-with-sum/description/
"""

class Solution:
    from collections import defaultdict
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(nums, goal):
            if goal<0:
                return 0
            s = 0
            count = 0
            l,r = 0,0
            while r<len(nums):
                s += nums[r]
                while s>goal and l<=r:
                    s -= nums[l]
                    l += 1
                count += r-l+1
                r += 1
            return count
        
        return helper(nums, goal) - helper(nums, goal-1)

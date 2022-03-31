# 209. Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
# Example 1: Input: target = 7, nums = [2,3,1,2,4,3] Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2: Input: target = 4, nums = [1,4,4] Output: 1
# Example 3: Input: target = 11, nums = [1,1,1,1,1,1,1,1] Output: 0

# Constraints:
# 1 <= target <= 10**9
# 1 <= nums.length <= 10**5
# 1 <= nums[i] <= 10**5
# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

from typing import List

class Solution:
    # with two pointers
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        left = 0
        subarr_len = 0
        subarr_minlen = 100000
        for i in range(0,len(nums)):
            sum += nums[i]

            while(sum >= target):
                subarr_len = i-left+1
                if subarr_len < subarr_minlen:
                    subarr_minlen = subarr_len
                sum -= nums[left]
                left += 1
                
        if subarr_minlen == 100000: 
            subarr_minlen = 0
        return subarr_minlen

if __name__ == "__main__":
    nums = list([2,3,1,2,4,3])
    target = 7
    # nums = list([10,5,13,4,8,4,5,11,14,9,16,10,20,8])
    # target = 80
    sol = Solution()
    print(sol.minSubArrayLen(target, nums))

# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Example 1: Input: nums = [2,7,11,15], target = 9 Output: [0,1] 
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2: Input: nums = [3,2,4], target = 6 Output: [1,2]
# Example 3: Input: nums = [3,3], target = 6 Output: [0,1]

# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

from typing import List


class Solution:
#  Hash table solution. Complexity O(n), but don't forget for hash search exec time
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, num in enumerate(nums):
            if num in hash:
                return [hash[num], i]
            else:
                hash[target-num] = i
        return(None)

    #  Two pointers solution. Complexity O(n*log(n))
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        arr_len = len(nums)
        # search for terms of target in sorted copy of array
        nums_sorted = sorted(nums)
        left = 0
        rigth = arr_len-1
        term1, term2 = None, None
        while left < rigth:
            if nums_sorted[left] + nums_sorted[rigth] == target:
                term1, term2 = nums_sorted[left], nums_sorted[rigth]
                break
            if nums_sorted[left] + nums_sorted[rigth] > target:
                rigth -= 1
            if nums_sorted[left] + nums_sorted[rigth] < target:
                left += 1
        # print(term1, term2)
        # search for positions of terms in original array
        x = y = None
        for i in range(arr_len):
            if nums[i] == term1 and x == None:
                x = i
            elif nums[i] == term2 and y == None:
                y = i

        return [x,y]

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    nums = [3,2,4]
    target = 6
    sol = Solution()
    print(sol.twoSum(nums, target))
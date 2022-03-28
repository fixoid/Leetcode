# 561. Array Partition I
# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

# Example 1: Input: nums = [1,4,3,2] Output: 4
# Explanation: All possible pairings (ignoring the ordering of elements) are:
# 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
# 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
# 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
# So the maximum possible sum is 4.

# Example 2: Input: nums = [6,2,6,5,1,2] Output: 9
# Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.

# Constraints:
# 1 <= n <= 104
# nums.length == 2 * n
# -104 <= nums[i] <= 104

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # sort List to make pairs from lower to higther
        nums.sort()
        # actualy we not need to find min in every pair,
        # because first number in every pair is lower than second
        return sum(nums[::2])

    def arrayPairSum2(self, nums: List[int]) -> int:
        # sort List to make pairs from lower to higther
        nums.sort()
        pointer = 0
        sum = 0
        while pointer < len(nums):
            # actualy we not need to find min in every pair,
            # because first number in every pair is lower than second
            # sum += min(nums[pointer], nums[pointer+1])
            sum += nums[pointer]
            # move pointer to next pair of numbers
            pointer += 2
        return sum


if __name__ == "__main__":
    some_list = list([6,2,6,5,1,2])
    print(some_list)
    sol = Solution()
    print (sol.arrayPairSum(some_list))

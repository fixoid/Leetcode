# 119. Pascal's Triangle II
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
# Example 1: Input: rowIndex = 3 Output: [1,3,3,1]
# Example 2: Input: rowIndex = 0 Output: [1]
# Example 3: Input: rowIndex = 1 Output: [1,1]
# Constraints:
# 0 <= rowIndex <= 33
# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

from nis import match
from typing import List
import math

class Solution:
    # calculating row by row with rewriting row
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 1:
            return [1,1]
        if rowIndex == 0:
            return [1]
        pascalRow = list(1 for x in range(rowIndex+1))
        for i in range(1,rowIndex):
            temp = 1
            for j in range(1,i+1):
                pascalRow[j],temp = pascalRow[j] + temp, pascalRow[j]

        return pascalRow
    
    # solution with direct row calculating by properties of pascal's triangle
    def getRow1(self, rowIndex: int) -> List[int]:
        pascalRow = list()
        pascalRow.append(1)
        if rowIndex > 1:
            pascalRow.append(rowIndex)
        if rowIndex > 3:
            pascalRow.append(rowIndex*(rowIndex-1)//2)
        if rowIndex > 5:
            pascalRow.append((rowIndex*(rowIndex-3+1)*(rowIndex-3+2))//6)
        if rowIndex > 7:
            factorial_row = math.factorial(rowIndex)
            factorial_k = math.factorial(3)
            # factorial_n_minus_k = math.factorial(rowIndex - 3)
            for i in range(4,rowIndex//2+1):
                factorial_k *= i
                # factorial_n_minus_k //= rowIndex - i + 1
                pascalRow.append(factorial_row//(factorial_k*math.factorial(rowIndex-i)))

        for i in range((rowIndex-1)//2,-1,-1):
            pascalRow.append(pascalRow[i])
        
        return pascalRow

if __name__ == "__main__":
    rowIndex = 15
    sol = Solution()
    for i in range(rowIndex+1):
        print(i, ": ",sol.getRow(i))




# 498. Diagonal Traverse
# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
# Constraints:
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# -105 <= mat[i][j] <= 105

from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        if m == 1:
            return mat[0]
        n = len(mat[0])
        ans = []
        if n == 1:
            for i in range(m):
                ans.extend(mat[i])
            return ans
        num = 1
        for k in range(n+m):
            if k % 2 == 0:
                for i in range(k - min(k, n), min(k, m)):
                    print(k)
                    ans.append(mat[i][k-i-1])
            else:
                for i in range(k - min(k, m), min(k, n)):
                    ans.append(mat[k-i-1][i])        
        return ans



if __name__ == '__main__':
    sol = Solution()
    # mat = [[1,2,3],[4,5,6],[7,8,9]]
    # mat = [[1,2,3]]
    # mat = [[1],[2],[3]]
    mat = [[2,5],[8,4],[0,-1]]
    print(sol.findDiagonalOrder(mat))
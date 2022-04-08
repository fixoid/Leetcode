# 6. Zigzag Conversion
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);
# Example 1: Input: s = "PAYPALISHIRING", numRows = 3 Output: "PAHNAPLSIIGYIR"
# Example 2: Input: s = "PAYPALISHIRING", numRows = 4 Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3: Input: s = "A", numRows = 1 Output: "A"
# Constraints:
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

class Solution:
    # The idea is to create some array [for rows] of array (of strings in our case) [for chars] and the pointer.
    def convert(self, s: str, numRows: int) -> str:
        direction = -1
        cur_row = 0
        rows = ["" for i in range(numRows)]

        for char in s:
            rows[cur_row] += char
            if cur_row == 0 or cur_row == (numRows-1):
                direction *= -1
            cur_row += direction
        
        return "".join(rows)

if __name__ == "__main__":
    s = "PAYPALISHIRING"
    sol = Solution()
    print(sol.convert(s,3))
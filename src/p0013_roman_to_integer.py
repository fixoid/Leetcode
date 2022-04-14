# 13. Roman to Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

class Solution:
    def romanToInt(self, s: str) -> int:
        int_rom = { "M": 1000, "D":500, "C":100, "L": 50, "X": 10, "V": 5, "I": 1 }
        ans = 0
        i = 0
        for i in range(len(s)-1):
            if int_rom[s[i]] >= int_rom[s[i+1]]:
                ans += int_rom[s[i]]
            else:
                ans -= int_rom[s[i]]
        ans += int_rom[s[len(s)-1]]
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("MMMCMXCIX"))
    # print(sol.romanToInt("MMMXCX"))
# 12. Integer to Roman
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.

class Solution:
    # Fast w/o division
    def intToRoman(self, num: int) -> str:
        int_rom = [ (1000, "M" ), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90,"XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I") ]
        ans = list()
        key_value = 0
        while (num > 0):
            if num - int_rom[key_value][0] >= 0:
                ans.append(int_rom[key_value][1])
                num -= int_rom[key_value][0]
            else:
                key_value += 1
        
        return "".join(ans)

    # Slow with division 
    def intToRoman1(self, num: int) -> str:
        int_rom = { 1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I" }
        ans = list()
        i = 0
        keys = list(int_rom.keys())
        while (num > 0):
            if num // keys[i] > 0:
                ans.append(int_rom[keys[i]])
                num -= keys[i]
            else:
                i += 1
        
        return "".join(ans)

if __name__ == "__main__":
    sol = Solution()
    # print(sol.intToRoman(4569))
    # print(sol.intToRoman1(4569))
    print(sol.intToRoman(4999))
    print(sol.intToRoman1(4999))
    # print(sol.intToRoman(4444))
    # print(sol.intToRoman1(4444))
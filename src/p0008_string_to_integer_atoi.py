# 8. String to Integer (atoi)
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
# The algorithm for myAtoi(string s) is as follows:
# 1.Read in and ignore any leading whitespace.
# 2.Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# 3.Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# 4.Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# 5.If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# 6.Return the integer as the final result.
# Note:
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.


class Solution:
    def myAtoi(self, s: str) -> int:
        intnum = 0
        digit_found = False
        mark = 1
        
        for char in s:
            # check for is not char from "0"(code: 48) to "9" (code: 57)
            if not(48 <= ord(char) <= 57):
                if not digit_found:
                    if ord(char) == 32:     # check for space char
                        pass
                    elif ord(char) == 45:   # check for "-" char
                        mark = -1
                        digit_found = True
                    elif ord(char) == 43:   # check for "+" char
                        digit_found = True
                    else:
                        break           # if char is not digit or " ", "+", "-", will stop
                else:
                    break           # if char is not digit, stop

            else:               # if char is digit, add it to answer
                intnum = intnum*10 + (ord(char)-48)
                if digit_found == False:
                    digit_found = True
        # check for max_int and return answer
        if mark == -1:
            return max(intnum*mark, -pow(2,31))
        else:
            return min(intnum, pow(2,31)-1)

if __name__ == "__main__":
    s = "-456 qwe r tyy 23"
    # s= "sdfff sf1"
    sol = Solution()
    print(sol.myAtoi(s))
    

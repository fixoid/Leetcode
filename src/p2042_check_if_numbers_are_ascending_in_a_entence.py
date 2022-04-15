# 2042. Check if Numbers Are Ascending in a Sentence
# A sentence is a list of tokens separated by a single space with no leading or trailing spaces. Every token is either a positive number consisting of digits 0-9 with no leading zeros, or a word consisting of lowercase English letters.
# For example, "a puppy has 2 eyes 4 legs" is a sentence with seven tokens: "2" and "4" are numbers and the other tokens such as "puppy" are words.
# Given a string s representing a sentence, you need to check if all the numbers in s are strictly increasing from left to right (i.e., other than the last number, each number is strictly smaller than the number on its right in s).
# Return true if so, or false otherwise.
# Example 1: Input: s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles" Output: true
# Explanation: The numbers in s are: 1, 3, 4, 6, 12. They are strictly increasing from left to right: 1 < 3 < 4 < 6 < 12.
# Example 2:Input: s = "hello world 5 x 5" Output: false
# Explanation: The numbers in s are: 5, 5. They are not strictly increasing.
# Example 3: Input: s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s" Output: false
# Explanation: The numbers in s are: 7, 51, 50, 60. They are not strictly increasing.
# Constraints: 3 <= s.length <= 200, s consists of lowercase English letters, spaces, and digits from 0 to 9, inclusive.
# The number of tokens in s is between 2 and 100, inclusive. The tokens in s are separated by a single space.
# There are at least two numbers in s. Each number in s is a positive number less than 100, with no leading zeros.
# s contains no leading or trailing spaces.


class Solution:
    # Time O(N), Space O(1). Looks not so good but only one run over string
    # and without using uild-in methods like str.split() and str.isdigit()  :-)
    def areNumbersAscending(self, s: str) -> int:
        curnum = 0
        prevnum = 0
        numcounter = 0
        digit_found = 0
        
        for i in range(len(s)):
            if digit_found == 0 or digit_found == 1:
            # check for is char from "0" (code: 48) to "9" (code: 57)
                if 48 <= ord(s[i]) <= 57:
                    curnum = curnum * 10 + (ord(s[i])-48)
                    if digit_found == 0:
                        digit_found = 1

                elif ord(s[i]) == 32 and digit_found == 1:  # if char is " " and digit(s) was before
                    if curnum > prevnum:
                        prevnum = curnum
                        curnum = 0
                        numcounter += 1
                    else:
                        return False
                else:
                    digit_found = -1
                    curnum = 0
            else:
                if ord(s[i]) == 32: # if char is " "
                    digit_found = 0
                    
        if curnum > prevnum > 0 or numcounter > 1:
            return True
        else:
            return False  


if __name__ == "__main__":
    s = " 4 5"
    # s= "sdfff sf1"
    sol = Solution()
    print(sol.areNumbersAscending("sunset is at 7 51 55 60 and 61 s 62"))
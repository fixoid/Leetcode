# 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        if x < 0:
            x = abs(x)
            mark = -1
        else: 
            mark = 1
        ans = 0
        max_int_div10 = pow(2,31) // 10

        while (x != 0):
            # poping digit
            digit = abs(x) % 10
            # overflow check
            if ans > max_int_div10:
                return 0
            # for positive int - last digit of maxint32 = 7, for negative = 8 
            if max_int_div10 == ans and (mark == 1 and digit > 7 or mark == -1 and digit > 8): 
                return 0
            # pushing digit to ans
            ans = ans*10 + digit
            x = x // 10
        return ans*mark

if __name__ == "__main__":
    sol = Solution()
    print(-8463847412, sol.reverse(-8463847412))
    print(-2147483648, sol.reverse(-2147483648))
    print(12345678, sol.reverse(12345678))

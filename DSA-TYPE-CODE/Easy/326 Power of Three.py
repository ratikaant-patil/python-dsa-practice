# 326. Power of Three

# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

# Example 1:

# Input: n = 27
# Output: true
# Explanation: 27 = 33
# Example 2:

# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.
# Example 3:

# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).
 

# Constraints:

# -231 <= n <= 231 - 1
 

# Follow up: Could you solve it without loops/recursion?

class SolutionFour:
    def isPowerOfThree(self, n:int)->bool:
        return n > 0 and 1162261467 % n == 0

    # LeetCode gives this constraint:
    # -2**31 <= n <= 2**31 - 1
    # The maximum positive number is: 2,147,483,647
    # Find the largest power of 3
    # 3²⁰ = 3,486,784,401
    # 3¹⁹ is smaller than the maximum integer.
    # 3²⁰ is larger than the maximum integer.

    # All powers of 3 divide 3¹⁹ exactly.
    # 1162261467 % 1  = 0
    # 1162261467 % 3  = 0
    # 1162261467 % 9  = 0
    # 1162261467 % 27 = 0
    # 1162261467 % 81 = 0

    # But:
    # 1162261467 % 2 = 1
    # 1162261467 % 5 = 2
    # 1162261467 % 6 = 3
    # So we can check whether a number divides the largest power of 3.

    # How to get Largest Number 
    #     
    # MAX = 2**31 - 1
    
    # power = 1
    
    # while power * 3 <= MAX:
    #     power *= 3
    
    # print(power)

obj4 = SolutionFour()
print(obj4.isPowerOfThree(27))

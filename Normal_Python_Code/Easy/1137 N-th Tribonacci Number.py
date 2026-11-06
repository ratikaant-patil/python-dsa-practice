# 1137. N-th Tribonacci Number

# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

 

# Example 1:

# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
# Example 2:

# Input: n = 25
# Output: 1389537
 

# Constraints:

# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

# <======================================== ANSWERS  #1 ========================================> 
class Solution:
    def tribonacci(self, n: int) -> int:
        if n <=2:
            return n

        a = 0
        b = 1
        c = 1
        for i in range(3,n+1):
            d = a + b + c
            a = b
            b = c
            c = d

        return d

obj = Solution()
print(obj.tribonacci(25))

# <======================================== ANSWERS  #2 ========================================> 
class SolutionTwo:
    def tribonacci(self, n: int) -> int:
        if n <=2:
            return n
        a , b , c = 0 , 1 , 1
        for _ in range(3,n+1):
            a , b , c = b , c , a + b + c
        return c

obj2 = SolutionTwo()
print(obj2.tribonacci(25))

# <======================================== ANSWERS  #3 ========================================> 
# Recursive Tree
class SolutionThree:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)

obj3 = SolutionThree()
print(obj3.tribonacci(25))
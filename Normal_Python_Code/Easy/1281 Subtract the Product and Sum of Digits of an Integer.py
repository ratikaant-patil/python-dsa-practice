# 1281. Subtract the Product and Sum of Digits of an Integer

# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

# Example 1:

# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15
# Example 2:

# Input: n = 4421
# Output: 21
# Explanation: 
# Product of digits = 4 * 4 * 2 * 1 = 32 
# Sum of digits = 4 + 4 + 2 + 1 = 11 
# Result = 32 - 11 = 21
 

# Constraints:

# 1 <= n <= 10^5


# <======================================== ANSWERS  #1 ========================================> 
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0

        while n > 0:
            reminder = n % 10
            product *= reminder
            sum += reminder
            n //= 10
        

        return product - sum

obj = Solution()
print(obj.subtractProductAndSum(4421))




# <======================================== ANSWERS  #1 ========================================> 
class SolutionTwo:
    def subtractProductAndSumTwo(self, n: int) -> int:
        product = 1
        sum = 0

        for i in str(n):
            product *= int(i)
            sum += int(i) 

        return product - sum

obj = SolutionTwo()
print(obj.subtractProductAndSumTwo(234))
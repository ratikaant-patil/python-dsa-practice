# 9. Palindrome Number

# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1
 

# Follow up: Could you solve it without converting the integer to a string?


# <======================================== ANSWERS  #1 ========================================> 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_copy = x
        ans = 0
        while x > 0:
            reminder = x % 10
            ans = ans * 10 + reminder
            x //= 10
        return True if x_copy == ans else False

obj = Solution()
print(obj.isPalindrome(141))


# <======================================== ANSWERS  #2 ========================================> 

# Using This Solution you only need to check half way not a full way of int
class SolutionTwo:
    def isPalindromeTwo(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverse = 0

        while x > reverse:
            reminder = x % 10
            reverse = reverse * 10 + reminder
            x //= 10

        return x == reverse or x == reverse // 10 

        

obj2 = SolutionTwo()
print(obj2.isPalindromeTwo(141))



#<======================================== ANSWERS  #2 ========================================> 

# Using This Solution you only need to check half way not a full way of int
class SolutionThree:
    def isPalindromeThree(self, x: int) -> bool:
        x_string = str(x)
        ans = x_string[::-1]
        return True if int(ans) == x else False

obj3 = SolutionThree()
print(obj3.isPalindromeThree(121))
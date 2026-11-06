# 509. Fibonacci Number

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:

# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:

# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

# Constraints:

# 0 <= n <= 30

# Fibonacci Series i simply by adding it last 2 number to get third number
# first number is 0 second is 1 then third become 1
# now second is 1 and third is 1 then fourth become 2
# now third is 1 and fourth is 2 then fith become 3 
# like this fibonaaci series works

# <======================================== ANSWERS  #1 ========================================> 

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1 :
            return n

        a , b = 0 , 1
        for _ in range(n):
            a , b = b , a + b

        return a

# Explanation :-
    # in this as you see we can a = 0 and b = 1 because starting two numbers are 0 & 1
    # After that we are interating our loop from 2 beacuse we have 1st and 2nd value which are 0 & 1
    # now in loop we are first adding sum of a + b in c 
    # then we are exhanging values in our given variable like a become 1 and b become 1
    # after that loop continoues we again get c = a + b which was 1 + 1 which is 2
    # then again exhanging values a become 1 and b become 2
    # like this we continoue to get our fibonacci answer

obj = Solution()
print(obj.fib(4))
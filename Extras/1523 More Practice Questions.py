# Level 1: Easy
# Question 1. Count even numbers in a range
# Problem: Given two integers low and high, count all even numbers between them (inclusive).

# Example:
# Input: low = 3, high = 10
# Output: 4

# Even numbers: 4, 6, 8, 10


# Your task: Write the formula without using a loop.

# Think about:
# - How do you count even numbers up to high?
# - How do you remove even numbers before low?
# - Do you need high + 1 or low - 1 ?

class Solution:
    def countEvenNumber(self,low:int,high:int)->int:
       return  high // 2 -  ( low - 1 )  // 2
        # In This we used ( low - 1 ) because it is possible that low number should be even and we dont have to minus it from high
        # Without ( low - 1)
        # high // 2 - low // 2       # high = 10 , low = 2
        # 10 // 2 - 2 // 2
        # 5 - 1
        # 4     # but from 2 to 10 their are 2,4,6,8,10 that total 5 count but we miss 2 because it also substracted from high because it is even number

        # with ( low - 1 )
        # hight // 2 - (low - 1) // 2
        # 10 // 2 - (2 - 1) // 2
        # 5 - (1) // 2
        # 5 - 0
        # 5    # We get corrected number because we substracted -1 from low because their are possibilites that low number should be even if odd no problem if even then we get issue

obj = Solution()
print(obj.countEvenNumber(4,10)) 
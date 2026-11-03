# 1523. Count Odd Numbers in an Interval Range

# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive). 

# Example 1:

# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].

# Example 2:

# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].

# Constraints:
# 0 <= low <= high <= 10^9


# <======================================== ANSWERS  ========================================> 
# Time complexity :- O(1)
# Space complexity :- O(1)

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2

obj = Solution()
print(obj.countOdds(1,8))

# <======================================== Explanation Of This  ========================================> 

# high // 2 = it will return all even values
# (hight + 1) // 2 = it will return all odd values
# for example :
#     high = 9
#    ( high // 2 = 4 ) # See here is what happining high is 9 and we want even number so it will basically returning how much times 
#                         high number is divisble by 2 
#                         1 % 2 = 1
#                         2 % 2 = 0
#                         3 % 2 = 1
#                         4 % 2 = 0
#                         5 % 2 = 1
#                         6 % 2 = 0
#                         7 % 2 = 1
#                         8 % 2 = 0
#                         # this get Skip because of it get calculate as 4.5 but we are asking int value (//) so it will return 4
#                         # but actual values are 5 for that we need to add +1 in high number so also include that number in count
#                         # if high value is even then +1 only addes 0.5 in so it will not get in result 
#                         # but if we add +1 in odd number then we get 1 which we will get count so we can not miss that high odd number
#                         # because of it
#                         9 % 2 = 1
#                         # Benifite of adding +1 is
#                         ( 9 + 1) // 2
#                         (10)//2 = 5 # Here We Get our high number which was odd in count thats why add +1 for odd number

# low // 2 = it will return how much extra number you counted and not needed in answer
# for example :
#        low = 3
#        high = 5
#        (high + 1) // 2 # it will now return 3 which was [1,3,5]
#        # But our low number is 3 and we dont want odd number before 3 so we minus it using
#        # (high + 1) // 2 - low // 2
#        # Using this we will get correct odd numbers 
   
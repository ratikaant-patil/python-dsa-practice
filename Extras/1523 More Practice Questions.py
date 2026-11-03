

# <======================================== Question  #1 ========================================>



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


# Basically in this formula ( high + 1 ) for getting odd values including high
# ( low - 1) fir getting even values including low
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




# <======================================== Question  #2 ========================================>

# Question 2. Count odd numbers in a range
# Problem: Count odd numbers between two given integers.
# Input: low = 8, high = 15
# Output: 4

# Odd numbers: 9, 11, 13, 15


# Your task: Solve it using mathematical division.

# Think about:
# - What happens if high is odd?
# - What happens if high is even?
# - Why did we use high + 1 in LeetCode 1523?

class SolutionTwo:
    def countOddNumber(self,low:int,high:int)->int:
       return ( high + 1 ) // 2 -  low // 2
    # In This we used ( high + 1 ) because it is possible that high number should be even or odd to check it we added this

obj2 = SolutionTwo()
print("odd number count is", end=' ')
print(obj2.countOddNumber(8,15)) 




# <======================================== Question  #3 ========================================>

# Question 3. Count multiples of 5
# Problem: Count all numbers divisible by 5 between low and high.
# Input: low = 4, high = 25
# Output: 5

# Numbers: 5, 10, 15, 20, 25


# Your task: Create a formula that works for any positive integer k.

# Think about:
# - How many multiples of 5 exist up to 25?
# - How many multiples of 5 exist before 4?
# - Should you use // 5 or // 4?

class SolutionThree:
    def countDivisible(self,low:int,high:int,divisible='')->int:
       # return high // 5 - ( low - 1 ) // 5
       # if you dont know what is divisible number then
       return high // divisible - ( low - 1 ) // divisible
    # In This we used ( high // divisible_number ) because we have to get how many number from high is divisble by divisible number
    # ( low - 1 ) // divisible_number because we have to know from lower how many numbers we dont have to count and ( low - 1) for also counting that number

obj3 = SolutionThree()
print("Divisible count is", end=' ')
print(obj3.countDivisible(4,25,4)) 




# <======================================== Question  #4 ========================================>


# Question 4. Count numbers divisible by 3 but NOT divisible by 2
# Problem: Count numbers between low and high that are divisible by 3 but not divisible by 2.
# Input: low = 1, high = 20
# Output: 4

# Numbers: 3, 9, 15

# Correction: Check the example carefully. There are actually 3 numbers, not 4.

# Your task: Build a formula without a loop.

# Think about:
# - First count multiples of 3.
# - Then remove numbers that are divisible by both 3 and 2.
# - What number is divisible by both 3 and 2?


class SolutionFour:
    def countDivisibleByNoDivisibleBy(self,low:int,high:int)->int:
        # My Logic
        #return high // 3 - (high // 3 // 2 + ( low - 1 ) // 3 // 2)

        # This is logic like first we calculate all number that are divisible by 3 then
                # We Substract numbers that are divisible by 3 and 2 also
                # in last we also substract how many external number i.e before low number are divisible by 3 and 2
                # high // 3 :- to get all divisible by 3 number
                # (high // 3 // 2) for getting numbers which are divisible by 3 and 2
                # ( low - 1 ) // 3 // 2 for getting before low number which is getting added

        # Chat GPT Improved LOGIC
        return (high // 3 - (low - 1) // 3) - (high // 6 - (low-1)//6)
        # Because 6 is a number which is only be divisible by 3 and 2
        # Next Time are just multiplication of it like 6 , 12 ,18
        
     

obj4 = SolutionFour()
print("Divisible By and Not Divisible By count is", end=' ')
print(obj4.countDivisibleByNoDivisibleBy(1,20)) 





# <======================================== Question  #5 ========================================>

# Question 5. Count numbers divisible by 3 OR 5
# Problem: Count numbers between low and high that are divisible by either 3 or 5.
# Input: low = 1, high = 20
# Output: 9

# Numbers:
# 3, 5, 6, 9, 10, 12, 15, 18, 20


# Your task: Solve it mathematically.

# Think about:
# - Count multiples of 3.
# - Count multiples of 5.
# - Are you counting 15 twice?
# - How can you avoid counting the same number twice?

class SolutionFive:
    def countDivisibleByOrBy(self,low:int,high:int)->int:
        # My Logic
        # return high // 3 + high // 5 - ((high // 3 // 5 ) - (low // 3 + low // 5 ) - ( low // 3 // 5))  
        
        # ChatGpt Correct Logic
        return (high // 3 - (low - 1) // 3) + (high // 5 - (low - 1) // 5) - (high // 15 - (low - 1) // 15)
        # This Concept is called Inclusion - Exclusion Principle
        # Count Multiples of 3 and count multiples of 5 then subtract multiples of 15
        # Because 3 * 5 = 15

obj5 = SolutionFive()
print("Divisible By 3 OR 5", end=' ')
print(obj5.countDivisibleByOrBy(1,20)) 
# class Solution:
#     def reverseNumber(self,num:int)->int:
#         ans = 0
#         while num > 0 :
#             rem = num % 10
#             ans = ans * 10 + rem
#             num//=10
#         return ans
      
# obj = Solution()
# print(obj.reverseNumber(1234))


# class SolutionTwo:
#     def reverseNumber(self,num:int)->int:
#         new = str(num)
#         ans = "0"
#         for i in new:
#             print(i)
#             ans = i + ans
#         return ans

        
      
# obj = SolutionTwo()
# print(obj.reverseNumber(1234))


class SolutionThree:
    def reverseNumber(self,num:int)->int:
        new = str(num)
        ans = new[::-1]
        # this is called string slicing it will work like 
        # new that is our variable name [start:end:step]
        # start mean which index from have to start slicing || end means on which index it should stop || and step means by 1 it go one-by-one and if -1 then it will go reverese order
        return ans
      
obj = SolutionThree()
print(obj.reverseNumber(1234))
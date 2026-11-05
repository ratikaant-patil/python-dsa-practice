class Solution:
    def reverseNumber(self,num:int)->int:
        ans = 0
        while num > 0 :
            rem = num % 10
            ans = ans * 10 + rem
            num//=10
        return ans
      
obj = Solution()
print(obj.reverseNumber(1234))
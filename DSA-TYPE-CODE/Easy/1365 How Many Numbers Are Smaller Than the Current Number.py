# 1365. How Many Numbers Are Smaller Than the Current Number

# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.

# Example 1:

# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 
# For nums[3]=2 there exist one smaller number than it (1). 
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
# Example 2:

# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]
# Example 3:

# Input: nums = [7,7,7,7]
# Output: [0,0,0,0]
 

# Constraints:
# 2 <= nums.length <= 500
# 0 <= nums[i] <= 100

# <======================================== ANSWERS  ========================================>

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        # Sort the array so each number's first index represents how many numbers are smaller.
        sorted_array = sorted(nums)

        # Store each number and its first occurrence index.
        count = {}

        # enumerate() gives both the index (i) and value (num) of each element in the sorted array.
        for i, num in enumerate(sorted_array):
            # Keep only the first index to handle duplicate numbers.
            if num not in count:
                count[num] = i

        # Return the count of smaller numbers for each element in original order.
        return [count[num] for num in nums]



        #     enumerate() gives us both the index and the value.
        # Index (i)	Number (num)
        #   0	             1
        #   1	             2
        #   2	             4
        #   3	             5
        #   4	             5
        
        # This is for preventing duplicate data
        
        # if num not in count:    
        #    count[num] = i


nums = [5,4,1,2,3]
obj = Solution()
print(obj.smallerNumbersThanCurrent(nums))

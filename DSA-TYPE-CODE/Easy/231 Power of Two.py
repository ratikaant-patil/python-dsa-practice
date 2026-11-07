# 231. Power of Two

# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

# Example 1:

# Input: n = 1
# Output: true
# Explanation: 20 = 1

# Example 2:

# Input: n = 16
# Output: true
# Explanation: 2**4 = 16
# Example 3:

# Input: n = 3
# Output: false
 

# Constraints:

# -231 <= n <= 231 - 1
 

# Follow up: Could you solve it without loops/recursion?

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and ( n & (n-1)) == 0

    #W hy does this work?
    # Every power of two has exactly one 1 in its binary representation.

    # For example:
    # Number	Binary
    #   1	     0001
    #   2	     0010
    #   4	     0100
    #   8	     1000
    #   16	     10000

    # When we subtract 1, all bits after that single 1 become 1.

    # Example: n = 16
    # n       = 10000
    # n - 1   = 01111
    #           -----
    # AND     = 00000

obj = Solution()
print(obj.isPowerOfTwo(16))
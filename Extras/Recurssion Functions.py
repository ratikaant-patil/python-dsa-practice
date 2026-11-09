#<===================== Question 1 ====================>

# Print 1 to 10 Using Recurssion
def printNumber(n):
    if n != 0:
        print(n , end=" ")
        printNumber(n-1)

# printNumber(10)


#<===================== Question 2 ====================>

# Print Factorial Using Recurssion
def fact(n):
    if n != 0:
        return n * fact(n-1)    
    return 1    

    # if n == 0:
    #     return 1    
    # return n * fact(n-1)

# print(fact(5))



#<===================== Question 3 ====================>

# Given an integer n, return its factorial using recursion.
# Input: n = 5
# Output: 120
def factorial(n):
    # Base Case
    if n!= 0:
        return n * factorial(n-1)
    return 1
# print("factorial is " ,factorial(5))


#<===================== Question 4 ====================>
# Given an integer n, return the sum of all its digits using recursion.
# Input: n = 1234
# Output: 10
def countSum(n):
    if n == 0:
        return 0

    # get last number
    digit = n % 10

    # remove last number
    n = n // 10

    return digit + countSum(n) 
# print(countSum(1234))

#<===================== Question 5 ====================>

# 3. Reverse a String
# Intermediate
# Given a string s, return the reversed string using recursion.

# Example:
# Input: s = "hello"
# Output: "olleh"

def reverseString(s):

    print("Entering:", s)

    if len(s) == 0:
        return ""

    result = s[-1] + reverseString(s[:-1])

    print("Returning:", result)

    return result


# print("Final:", reverseString("hello"))


# 4. Check Whether an Array Is Sorted
# Intermediate
# Given an integer array, determine whether the array is sorted in non-decreasing order using recursion.

# Example:
# Input: nums = [1, 2, 3, 4, 5]Output: True

def findSortedArray(arr):

    if len(arr) <= 1:
        return True

    if arr[0] > arr[1]:
        return False

    print(arr)

    return findSortedArray(arr[1:])


print(findSortedArray([1, 2, 3, 4, 5]))



# 5. Generate All Subsets of an Array
# Advanced
# Given an integer array nums containing unique elements, return all possible subsets (the power set) using recursion.

# Example:
# Input: nums = [1, 2]Output: [[], [1], [2], [1, 2]]
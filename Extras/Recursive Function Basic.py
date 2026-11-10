# Level 1: Understand recursion
# 1. Print numbers from 1 to N

# Given an integer n, print numbers from 1 to n.
# Input: n = 5
# Output: 1 2 3 4 5

def printOnetoFive(n):
    # Base Condition
    if n<=0:
        return 0
    
    printOnetoFive(n-1)
    print(n, end=" ")


printOnetoFive(5)


# 2. Print numbers from N to 1

# Given an integer n, print numbers in reverse order.
# Input: n = 5Output: 5 4 3 2 1

print()
print()

def printNtoOne(n):
    # Base Condition
    if n<=0:
        return 0

    print(n, end=" ")
    printNtoOne(n-1)

printNtoOne(5)


print()
print()

def printNtoOne(n):
    # Base Condition
    if n<=0:
        return 0

    print(n, end=" ")
    printNtoOne(n-1)

printNtoOne(5)


print()
print()

def printNtoOne(n):
    # Base Condition
    if n<=0:
        return 0

    print(n, end=" ")
    printNtoOne(n-1)

printNtoOne(5)


print()
print()

def printNtoOne(n):
    # Base Condition
    if n<=0:
        return 0

    print(n, end=" ")
    printNtoOne(n-1)

printNtoOne(5)

print()
print()

def printNtoOne(n):
    # Base Condition
    if n<=0:
        return 0

    print(n, end=" ")
    printNtoOne(n-1)

printNtoOne(5)

print()
print()

def printNtoOne(n):
    # Base Condition
    if n<=0:
        return 0

    print(n, end=" ")
    printNtoOne(n-1)

printNtoOne(5)

print()
print()

def printNtoOne(n):
    # Base Condition
    if n<=0:
        return 0

    print(n, end=" ")
    printNtoOne(n-1)

printNtoOne(5)

print()
print()

def printNtoOne(n):
    # Base Condition
    if n<=0:
        return 0

    print(n, end=" ")
    printNtoOne(n-1)

printNtoOne(5)

# ewfwefw

# 3. Sum of first N natural numbers

# Calculate the sum of numbers from 1 to n.
# Input: n = 5Output: 15# 1 + 2 + 3 + 4 + 5 = 15



# Level 2: Basic logic
# 4. Factorial of a number

# Calculate the factorial of a given number.
# Input: n = 5Output: 120# 5 * 4 * 3 * 2 * 1 = 120



# 5. Calculate the power of a number

# Calculate base raised to the power exponent.
# Input: base = 2, exponent = 4Output: 16# 2 * 2 * 2 * 2 = 16



# 6. Count digits in a number

# Count how many digits are present in an integer.
# Input: n = 12345Output: 5



# Level 3: Slightly challenging
# 7. Sum of digits

# Calculate the sum of all digits in a number.
# Input: n = 1234Output: 10# 1 + 2 + 3 + 4 = 10



# 8. Reverse a string

# Reverse a given string using recursion.
# Input: s = "hello"Output: "olleh"



# 9. Check whether a string is palindrome

# Check whether a string reads the same forward and backward.
# Input: s = "madam"Output: TrueInput: s = "hello"Output: False



# 10. Find the largest element in an array

# Find the maximum element using recursion.
# Input: arr = [10, 25, 5, 40, 15]Output: 40
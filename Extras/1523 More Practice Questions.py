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
# - Do you need high + 1 or low - 1?


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


# Level 2: Medium

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


# Level 3: Challenge


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

#! 1. Recursion Practice: Factorial

# # Task:
# # Write a function factorial(n) that returns n!
# # Example: factorial(5) = 120

# # Input: integer n 5
# # Output: integer the factorial of n -> 120

# # ----------------------------
# # What is factorial?
# # Factorial of n  n! is the product of all positive integers from n down to 1.

# # Examples:
# # 5! = 5 × 4 × 3 × 2 × 1 = 120
# # 4! = 4 × 3 × 2 × 1 = 24
# # 3! = 3 × 2 × 1 = 6
# # 2! = 2 × 1 = 2
# # 1! = 1
# # Special case: 0! = 1 
# #
# # General formula:
# # n! = n × (n-1) × (n-2) × ... × 1
# # ----------------------------

# # ----------------------------
# # Recursive pattern:
# # Factorial naturally fits recursion because:
# # - Recursive case: n! = n × (n-1)!
# # - Base case: 1! = 1 (or 0! = 1)

# # Example breakdown:
# # 5! = 5 × 4!
# # 4! = 4 × 3!
# # 3! = 3 × 2!
# # 2! = 2 × 1!
# # 1! = 1  <-- base case reached

# # Then recursion "unwinds":
# # 2! = 2 × 1 = 2
# # 3! = 3 × 2 = 6
# # 4! = 4 × 6 = 24
# # 5! = 5 × 24 = 120

# # Visualization: 
# # factorial(5)
# #  → 5 * factorial(4)                     # 5 * 24 = 120  
# #       → 4 * factorial(3)                # 4 * 6 = 24  
# #            → 3 * factorial(2)           # 3 * 2 = 6  
# #                 → 2 * factorial(1)      # 2 * 1 = 2  
# #                      → 1   (base case)  # 1

# # 1 → 2 → 6 → 24 → 120

# # ----------------------------

# def factorial(n):
#     """
#     Returns the factorial of n using recursion.
#     Base case: if n <= 1, return 1
#     Recursive case: return n * factorial(n-1)
#     """
#     # print("n:", n)
#     if n <= 1:  # base case
#         return 1
    
#     res = n * factorial(n - 1)  # recursive case
    
#     # print("res:", res )
    
#     return res



# print(factorial(5))  # Expected output: 120

# # Only when the base case returns 1 do the calculations actually start:

# # factorial(2) = 2 * 1 = 2

# # factorial(3) = 3 * 2 = 6

# # factorial(4) = 4 * 6 = 24

# # factorial(5) = 5 * 24 = 120



#! 2. Recursion Practice: Sum of numbers 1..n

# Task:
# Write a function sum_n(n) that returns the sum of numbers from 1 up to n.
# Example: sum_n(4) = 10
#
# Input: integer n (e.g., 4)
# Output: integer (the sum from 1 through n, e.g., 10)
#
# ----------------------------
# What is this problem?
# Add all numbers from 1 to n:
#
# Example:
# sum_n(4) = 1 + 2 + 3 + 4 = 10
# sum_n(5) = 1 + 2 + 3 + 4 + 5 = 15
#
# ----------------------------
# Recursive pattern:
# - Recursive case: sum_n(n) = n + sum_n(n-1)
# - Base case: sum_n(1) = 1
#
# Example breakdown:
# sum_n(4) = 4 + sum_n(3)
# sum_n(3) = 3 + sum_n(2)
# sum_n(2) = 2 + sum_n(1)
# sum_n(1) = 1   <-- base case
#
# Then recursion "unwinds":
# sum_n(2) = 2 + 1 = 3
# sum_n(3) = 3 + 3 = 6
# sum_n(4) = 4 + 6 = 10
# ----------------------------

def sum_n(n):
    """
    Returns the sum of numbers from 1 up to n using recursion.
    Base case: if n == 1, return 1
    Recursive case: return n + sum_n(n-1)
    """
    if n <= 1:  # base case
        return 1
    return n + sum_n(n - 1)  # recursive case


# Example runs
print(sum_n(4))  # Expected output: 10
print(sum_n(5))  # Expected output: 15

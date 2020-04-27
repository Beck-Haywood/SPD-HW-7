"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

def isPalindrome(x, left, right):
    """
    :type x: int
    :rtype: bool
    """
    # Check if empty
    if x == "":
        return True
    # Base Case
    if left == right:
        return True
    if x[left] != x[right]:
        return False
    if left < right:
        return isPalindrome(x, left + 1, right - 1)
    return True

print(isPalindrome(10, 0, len(10) - 1))
print(isPalindrome(101, 0, len(10) - 1))
print(isPalindrome(0, 0, len(10) - 1))
print(isPalindrome(100000000000000000001, 0, len(10) - 1))
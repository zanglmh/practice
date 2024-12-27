"""
Given an integer x, return true if x is a palindrome, and false otherwise.

To run file, python Palindrome.py input.txt
The first line in input.txt should contain the integer x.
"""

class Solution(object):
    def isPalindrome(self, x):
        # Declare variables
        reverse = 0
        num = x

        # Return False default, NOT palindrome
        if x < 0:
            return False
        while x > 0:
            # Store each digit of the number reversely
            reverse = (reverse * 10) + x % 10
            x = x // 10

        return reverse == num

def main():
    import sys

    if len(sys.argv) != 2:
        print("Usage: python Palindrome.py <input_file>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, "r") as file:
            # Read the first line as the integer input
            x = int(file.readline().strip())

        # Solve the problem using the Solution class
        solution = Solution()
        result = solution.isPalindrome(x)

        # Print the result
        print(f"Input: x = {x}")
        print(f"Output: {result}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

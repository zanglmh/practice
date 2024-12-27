"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Given a Roman numeral, convert it to an integer.

To run file, python RomanToInt.py input.txt
The first line in input.txt should contain the Roman numeral.
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        ans = 0

        # Replace subtraction-based numerals with expanded form
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        
        # Add the values of each character
        for char in s:
            ans += translations[char]
        
        return ans

def main():
    import sys

    if len(sys.argv) != 2:
        print("Usage: python RomanToInt.py <input_file>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, "r") as file:
            # Read the first line as the Roman numeral input
            roman = file.readline().strip()

        # Solve the problem using the Solution class
        solution = Solution()
        result = solution.romanToInt(roman)

        # Print the result
        print(f"Input: Roman numeral = {roman}")
        print(f"Output: Integer = {result}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

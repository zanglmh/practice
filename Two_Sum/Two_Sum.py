import sys

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

"""
To run file, python Two_Sum.py input.txt
First line input & Second line target in input.txt
"""

class Solution:
    # This function replicates your Java solution
    def twoSum(self, nums, target):
        sum_value = 0
        answer_index = [-1, -1]
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                sum_value = nums[i] + nums[j]
                if sum_value == target:
                    answer_index[0] = i
                    answer_index[1] = j
                    return answer_index
        return answer_index  # Return default if no solution is found

def main():
    if len(sys.argv) != 2:
        print("Usage: python twosum.py <input_file>")
        sys.exit(1)
    
    # Read the filename from command-line arguments
    filename = sys.argv[1]

    try:
        # Load the input data from the text file
        with open(filename, "r") as file:
            lines = file.readlines()
            nums = list(map(int, lines[0].strip().split(",")))  # First line: nums
            target = int(lines[1].strip())  # Second line: target

        # Solve the problem using the Solution class
        solution = Solution()
        result = solution.twoSum(nums, target)

        # Print the results
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Output: {result}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

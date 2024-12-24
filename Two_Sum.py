"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
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

# Function to run the solution with example inputs
if __name__ == "__main__":
    # Example arguments
    nums = [2, 7, 11, 15]
    target = 9

    # Create a Solution instance and run the method
    solution = Solution()
    result = solution.twoSum(nums, target)

    # Print the results
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")

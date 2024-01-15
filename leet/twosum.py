# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Constraints:
#    2 <= nums.length <= 10^4
#    -109 <= nums[i] <= 10^9
#    -109 <= target <= 10^9


def twoSum(nums: list[int], target: int) -> list[int]:
    # Store the index of each number in a map 
    # like {2: 0, 7: 1, 11: 2, 15: 3} in the above example for nums = [2,7,11,15]
    # the key is the number and the value is the index
    numMap = {}
    for i, n in enumerate(nums):
        numMap[n] = i

    for i, n in enumerate(nums, start=0):
        if target - n in numMap and numMap[target - n] != i:
            return [i, numMap[target - n]]


if __name__ == "__main__":
    print(
        twoSum(
            [2,7,11,16],
            9,
        )
    )

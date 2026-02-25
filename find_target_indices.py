#Question:given a list of numbers, find the indices of two numbers that add up to a specific target.

def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print("Indices of numbers:", result)
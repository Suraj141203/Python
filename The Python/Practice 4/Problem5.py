# Task 5:
# Given list: nums = [1, 2, 3, 2, 5]
# Check if duplicate element exists in the list

nums = [1, 2, 3, 2, 5]

# Convert list to set (set removes duplicates)
if len(nums) != len(set(nums)):
    print("Duplicate found")
else:
    print("No duplicate found")
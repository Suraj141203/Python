# Task 4:
# Given list: nums = [1, 2, 3, 4, 5, 6]
# Print only even numbers from the list

nums = [1, 2, 3, 4, 5, 6]

for num in nums:
    if num % 2 == 0:   # Check if number is divisible by 2
        print("Even number:", num)
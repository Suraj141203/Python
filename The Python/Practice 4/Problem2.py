# Take 5 Numbers By Users And Store inside the list 
# Print the sum of whole numbers
# Print The Average Also

numbers = []

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)

print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)
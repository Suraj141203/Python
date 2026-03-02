# All Important List Methods Demonstration (Using Different Variables)

print("----- append() -----")
# Adds element at end (Modifies list, Returns None)
x1 = [1, 2, 3]
result1 = x1.append(4)
print("Return Value:", result1)
print("Updated List:", x1)


print("\n----- remove() -----")
# Removes first occurrence (Modifies list, Returns None)
x2 = [1, 2, 3]
result2 = x2.remove(2)
print("Return Value:", result2)
print("Updated List:", x2)


print("\n----- pop() -----")
# Removes element by index (Modifies list, Returns removed value)
x3 = [10, 20, 30]
result3 = x3.pop(1)
print("Return Value:", result3)
print("Updated List:", x3)


print("\n----- sort() -----")
# Sorts list (Modifies list, Returns None)
x4 = [5, 2, 8, 1]
result4 = x4.sort()
print("Return Value:", result4)
print("Sorted List:", x4)


print("\n----- reverse() -----")
# Reverses list (Modifies list, Returns None)
x5 = [1, 2, 3]
result5 = x5.reverse()
print("Return Value:", result5)
print("Reversed List:", x5)


print("\n----- index() -----")
# Finds index (Does NOT modify list, Returns index)
x6 = [10, 20, 30]
result6 = x6.index(20)
print("Return Value:", result6)
print("Original List:", x6)


print("\n----- count() -----")
# Counts occurrences (Does NOT modify list, Returns count)
x7 = [1, 2, 2, 3]
result7 = x7.count(2)
print("Return Value:", result7)
print("Original List:", x7)


print("\n----- extend() -----")
# Adds multiple elements (Modifies list, Returns None)
x8 = [1, 2]
result8 = x8.extend([3, 4])
print("Return Value:", result8)
print("Updated List:", x8)


print("\n----- insert() -----")
# Inserts element at specific index (Modifies list, Returns None)
x9 = [10, 20, 30]
result9 = x9.insert(1, 15)
print("Return Value:", result9)
print("Updated List:", x9)


print("\n----- clear() -----")
# Removes all elements (Modifies list, Returns None)
x10 = [1, 2, 3]
result10 = x10.clear()
print("Return Value:", result10)
print("Updated List:", x10)
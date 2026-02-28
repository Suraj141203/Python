# Comparison Between List and Tuple

print("----- LIST EXAMPLE -----")

my_list = [10, 20, 30]
print("Original List:", my_list)

# List is mutable (can change)
my_list.append(40)
my_list[0] = 100
print("Modified List:", my_list)

print("\n----- TUPLE EXAMPLE -----")

my_tuple = (10, 20, 30)
print("Original Tuple:", my_tuple)

# Tuple is immutable (cannot change)
try:
    my_tuple[0] = 100   # This will cause error
except TypeError as e:
    print("Error:", e)

print("Tuple after attempt:", my_tuple)

print("\n----- METHODS COMPARISON -----")

print("List Methods Example:")
print("Count in List:", my_list.count(20))
print("Index in List:", my_list.index(20))

print("\nTuple Methods Example:")
print("Count in Tuple:", my_tuple.count(20))
print("Index in Tuple:", my_tuple.index(20))
# And Operator
# True and True   → True
# True and False  → False

# Or Operator
# True or False  → True
# False or False → False

#NOT Operator
#not True  → False
# not False → True


# Logical Operators Combined Example

age = 20
has_id = True
is_member = False

# AND Operator
if age >= 18 and has_id:
    print("AND: Entry Allowed")
else:
    print("AND: Entry Denied")

# OR Operator
if age < 18 or is_member:
    print("OR: Special Access")
else:
    print("OR: No Special Access")

# NOT Operator
if not is_member:
    print("NOT: You are not a member")
else:
    print("NOT: You are a member")

# Combined Logical Operators
if age >= 18 and (has_id or is_member):
    print("COMBINED: Full Access Granted")
else:
    print("COMBINED: Access Denied")

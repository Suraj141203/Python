# Write a program to detect the double space in a string.
letter = """Dear <|Name|>,
You are selected!
\t<|Date|>"""

print(letter.replace("<|Name|>", "Suraj").replace("<|Date|>", "20 Feb 2026"))

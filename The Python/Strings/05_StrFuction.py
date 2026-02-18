# Here I Practice Most Of The String Function 

text = "HELLO"
print(text.lower())  # It converts uppercase letters to lowercase

text1 = "hello"
print(text1.upper())  # It converts lowercase letters to uppercase

name = "   Suraj   "
print(name.strip())  # It removes extra spaces from beginning and end

text2 = "I love Java"
print(text2.replace("Java", "Python"))  # It replaces a word with another word

text3 = "Python is easy"
print(text3.split())  # It splits string into a list using space as default separator

name2 = "Suraj"
print(name2.find("r"))  # It finds position (index) of character in string

text4 = "banana"
print(text4.count("a"))  # It counts how many times a character appears

text5 = "Python"
print(text5.startswith("Py"))  # It checks if string starts with given value

text6 = "Python"
print(text6.endswith("on"))  # It checks if string ends with given value

text7 = "Suraj"
print(text7.isalpha())  # It checks if string contains only alphabets

num = "1234"
print(num.isdigit())  # It checks if string contains only digits

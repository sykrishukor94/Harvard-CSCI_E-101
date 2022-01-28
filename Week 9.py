# Week 9 Section
# String Manipulation
#string concatenation

string_1 = "Hello"
string_2 =" World"
string_3 = string_1 +string_2
print(string_3)

s2 =""
for s in string_1:
    s2 = s2 + s

print(s2)

# str slicing
string_4 = "hello@gmail.com"

splits = string_4.split('@')

print(splits)
splits[1][0:]

# testing str
print(string_4)

if '@' in string_4:
    print("Yes @ is in " +string_4)

if '!' not in string_4:
    print(" ! not  in " +string_4)

# String methods to know
# isalnum()
#
# isalpha()
#
# isdigit()
#
# islower()
#
# isspace()
#
# isupper()

s5 = "Hello5World"
s5.isalnum()

s5 = "Hello5World@"
s5.isalnum()

# Methods to modify string
# # lower()
# #
# # upper()
# #
# # strip()
# #
# # strip(c)

s5 = " Hello5World@ "
s5.strip()

s5 = "Hello5World@"
s5.strip('@')

# Searching strings
# endswith(substring)
#
# find(substring)
#
# startswith(substring)
#
# replace(old_string, new_string)

#Examples

s6 = "hello@gmail.com"

s6.endswith(".com")

s7 = "www.google.com"
s7.startswith("www")
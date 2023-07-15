str1 = "arya Salecha is Good Boy123."

# String is Immutable (Not Changeble)

print(str1.casefold())   # arya salecha is good boy123.
print(len(str1))   # 28
print(str1.center(40,'*'))   # ******Arya Salecha is Good Boy123.******
print(str1.count(' '))  # 4
print(str1.count('a',5))  # 2

str1 = "arya Salecha is Good Boy123."
print(str1.endswith("2."))  # False

str2 = "Ståle"
print(str2.encode())  # b'St\xc3\xa5le'
print(str2.encode(encoding="ascii",errors="namereplace"))  # b'St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
print(str2.encode(encoding="ascii",errors="replace"))  # b'St?le'
print(str2.encode(encoding="ascii",errors="ignore"))  # b'Stle'
print(str2.encode(encoding="ascii",errors="xmlcharrefreplace"))  # b'St&#229;le'
print(str2.encode(encoding="ascii",errors="backslashreplace"))  # b'St\\xe5le'

str1 = "arya Salecha\tis Good Boy123." 
print(str1.expandtabs(12))  # arya Salecha            is Good Boy123.


str1 = "{name} {surname} is GOod Boy.".format(name = "Manoj", surname = "Salecha")
print(str1)   # Manoj Salecha is GOod Boy.


dict1 = {'Name' : "Krutarth", 'surname' : 'Patel'}
str1 = "{Name} {surname} is GOod Boy.".format_map(dict1)  # Manoj Salecha is GOod Boy.
print(str1)


print(str1.find('is'))  # -1
print(str1.index('is'))  # 15   # Error if is not Found


str1 = "Arya_Salecha123"
print(str1.isalpha())  # False
print(str1.isnumeric())  # False

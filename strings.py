str1 = "Arya Salecha"

str2 = 'd'
print(type(str2))   # <class 'str'>
print(type(str1))   # <class 'str'>

print(id(str2))  # 1420450385072
print(str1.__sizeof__())   # 61
print(len(str1))  # 12   # Length starts from 1, Index starts from 0

str2 = "Royal_is Best Institute Ever123."

# Indexing
print(str2[1]) # o
print(str2[-2]) # 3
print(str2[4]) # l

# Slicing

# print(str2[start : end (n-1) : step (n-1)])
print(str2[1 : 5])   # oyal
print(str2[4:5])  # l
print(type(str2[4:5]))  # <class 'str'>

print(str2[10:5])  # blank
print(str2[-3:5:2])  # blank
print(str2[10:4:-2])  # e i
print(str2[10:4:2])  # 
print(str2[-6::-3])  # e utIs _y
print(str2[5::-1])  # _layoR



# String Methods

str2 = "Royal_is Besti Institute Ever123."

# String is Immutable (Not Changeble)
# str3 = "Ayan"
# print(id(str3))
# str3+=str2
# print(id(str3))
# print(str3)  # AyanRoyal_is Best Institute Ever123.

print(str2.replace("3", '67'))   # Royal_is Best Institute Ever1267.
print(str2.replace("e", 'o',1))   # Royal_is Bost Institute Ever123.

print(str2.capitalize())   # Royal_is best institute ever123.
print(str2.casefold())   # royal_is best institute ever123.
print(str2.swapcase())   # rOYAL_IS bEST iNSTITUTE eVER123.
print(str2.lower())   # royal_is best institute ever123.
print(str2.upper())   # ROYAL_IS BEST INSTITUTE EVER123.
print(str2.title())   # Royal_Is Best Institute Ever123.

print(str2.count("i"))  # 2
print(str2.count("z"))  # 0
print(str2.index('i'))  # 6
print(str2.rindex('i'))  # 18
print(str2.index('i',7))  # 13
print(str2.rindex('i',7,14))  # 13
print(str2.find('i',7,14))  # 13
print(str2.find('z',7,14))  # -1
# print(str2.index('z',7,14))  # Error


str3 = "the lion is the king of the Jungle."
# o/ p = "a lion is the king of a Jungle."

str3 = str3.replace('the','a',1)
list1 = str3.split()
print(list1)  # ['a', 'lion', 'is', 'the', 'king', 'of', 'the', 'Jungle.']

list1.reverse()

for i in range(len(list1)):
    if list1[i] == 'the':
        list1[i] = 'a'
        break

list1.reverse()

str1 = ' '.join(list1)

print(str1)  # a lion is the king of a Jungle.




l1 = [19, 19, 15, 5, 5, 5, 1, 2]


for i,j in enumerate(l1,1):
    if len(l1) == 8 and i == 5 and l1.count(l1[i]) == 3:
        print(True)

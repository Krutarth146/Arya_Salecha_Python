# 1. Arithmetic Operators + - * / // % **

# 2. Logical Operators   and or not

# 3. Bitwise Operators    & | ^ << >>

# 4. Comparison O/p  == < > <= >= != 

# 5. Assignment Operators = += -= *= /= //= %= **= <<= >>=  (Priority Low)

# 6. Memebership O/p  in , not in   

# 7. Identity O/p   is, is not

'''

'''

print(""" cs""")
print((2**3)**2)   # 512

print(21 >> 4)
print(21 and 4)
print(21 and 43)
print(21 or 43)
print(not(not 2))






list1 = [90,23,45,12,89]

for i in range(10):
    print(i,end=' ')   # 0 1 2 3 4 5 6 7 8 9
print()
for i in range(2,12):
    print(i,end=' ')   #2 3 4 5 6 7 8 9 10 11

print()
for i in range(12,2):
    print(i,end=' ')   # blank

print()
for i in range(-7,-2):
    print(i,end=' ')   # -7 -6 -5 -4 -3

print()
for i in range(2,7,3):
    print(i,end=' ')   # 2 5

print()
for i in range(99,0,-2):
    if i % 5 == 0:
        print(i,end=' ')   # 95 85 75 65 55 45 35 25 15 5

print()
for i in range(-40,4,3):
    print(i,end=' ')   # -40 -37 -34 -31 -28 -25 -22 -19 -16 -13 -10 -7 -4 -1 2
       

list1 = [90,23,45,12,89]

print()
for i in list1:
    if i == 89:
        print("ELement is found")

if 89 in list1:
    print("ELement is found")

x = 900
y = 900

# print(id(x))  # 3026617540496
# print(id(y))  # 3026617540496

# if x == y:
#     print("X is y")


list1 = [10,20,30,40]
list2 = [10,20,40,30]

print(id(list1))  # 1705612138752
print(id(list2))  # 1705612293120

list1.sort()
list2.sort()

if list1 == list2:
    print("Same")

if list1 is list2:   # Identity Operator
    print("same with equals to")

print(chr(65))  # A
print(chr(122))  # z

print(ord('Z'))  # 90



num1 = 90
num2 = 332
num3 = 2111

max = num1 if num1 > num2 else num2  # Task 3 num compare
print(max)
# if num1 > num2: 
#     if num1 > num3:
#         print(num1,"is Max")
#     else:
#         print(num3,"is Max")
# else:
#     if num2 > num3:
#         print(num2,"is Max")
#     else:
#         print(num3,"is Max")

# list1 = [230,405,10,20,40,1]
# list1.sort(reverse=True)
# # list1.reverse()
# print(list1)


# choice= 'R'

# match choice:
#     case 5: print("5 is selected")

#     case 32.90: print("csdvsdv")

#     case other: print("Wild Card")


# Elif


num = 0

if num > 0:
    print("num is Positive")
elif num == 0:
    print("num is Negative")
# list1 = [10,20,30,40,50]

# # Linear Search
# user_need = int(input("ENter Element: "))
# arya = 0
# for i in list1:
#     if i == user_need:
#         arya = 1
#         break
#     else:
#         arya = 0

# if arya == 1:
#     print("Element is Found")
# else:
#     print("Element is Not Found")

# if user_need in list1:    # Membership o/p   in, not in
#     print("Element is Found")
# else:
#     print("Element is Not Found") 



x = 90
y = 90

if x == y:
    print("x == y")

if x is y:
    print("x is y")   # Identity O/p


list1 = [10,20,30,405]
list2 = [10,20,30,405]

if list1 is list2:
    print("list1 is list2")
else:
    print("Fail")

print(id(list1))  # 2550855620864
print(id(list2))  # 2550855775232


if list1 == list2:
    print("Same")

else:
    print("Not Same")


# Prime Numbers

# 23 -> 1,23
# 24 -> 1,2,3,4,6,8,12,24

num = 24
factors = 0

for i in range(1,num+1):
    if num % i == 0:
        factors+=1

print(factors)
if factors == 2:
    print("Prime Number")


# Perfect Number


for num in range(1,10001):   # num = 34
    sum = 0

    for i in range(1,num):  # 1 to 33
        if num % i == 0:   # 34 % 1 to 33
            sum += i 

    if sum == num:
        print(num)


# Palindrome, Armstrong, Twin, Sum of Digits, total Digits, Power, Factorial, fibonacci
def square(num):
    return num*num

print(square(56))  # 3136


sq_1 = lambda num : num*num
print(sq_1(77))  # 5929


list1 = [10,90,67,342,21]
list2 = []
for i in list1:
    list2.append(sq_1(i))


print(list2)


# Powerful Functions ----> Map, Reduce, Filter

sq1 = map(square, list1)

print(sq1)   # <map object at 0x000001FCDA1EC640>

def square(num):
    return num*num

list1 = [10,90,67,342,21]

sq1 = list(map(square, list1))

print(sq1)   # [100, 8100, 4489, 116964, 441]


# print(list(map(lambda x : x*x, list1)))



# list1 = [10,90,89,56,32]

# sq1 = list(map(square, list1))
# print(sq1)  # [100, 8100, 7921, 3136, 1024]


# # -----------------------------------------------------------------

# print(list1)   # [10, 90, 89, 56, 32]

# k1 = list(filter(lambda x : x >= 50, list1))  # [342]
# print(k1)   # [90, 89, 56]

# k1 = list(map(lambda x : x >= 50, list1))
# print(k1)  # [False, True, True, True, False]


# # -----------------------------------------------------------

# from functools import reduce

# ans = reduce(lambda x,y : x+y, list1)   # [10, 90, 89, 56, 32]

# print(ans)  # 277


# from itertools import accumulate

# res = list(accumulate( list1, lambda x,y : x+y))
# print(res)   # [10, 100, 189, 245, 277]


# # ---------------------------------------------------


# list1 = [10,20,30,405,90]

# ans = [i+500 for i in list1]
# print(ans)   # [510, 520, 530, 905, 590]


# ans1 = list(map(lambda x:x+500, list1))
# print(ans1)

# l9 = [int(i) for i in input().split()]
# print(l9)   # [21, 90, 78, 56, 45, 34]


# print(list(map(int, input().strip().split())))


list1 = [10,20,30,405,90]
x = list(map(lambda x:x%2, list1))
x = list(filter(lambda x:x%2, list1))

x = list(filter(lambda x:x%2==0, list1))
# x = list(map(lambda x:x%2==0, list1))
print(x)   # [0, 0, 0, 1, 0]


from functools import reduce

list1 = [10,90,23,56,44,77]

x = reduce(lambda x,y : x+y, list1)
print(x)   # 300


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


print(list(map(lambda x : x*x, list1)))



list1 = [10,90,89,56,32]

sq1 = list(map(square, list1))
print(sq1)  # [100, 8100, 7921, 3136, 1024]


# -----------------------------------------------------------------

print(list1)   # [10, 90, 89, 56, 32]

k1 = list(filter(lambda x : x >= 50, list1))  # [342]
print(k1)   # [90, 89, 56]

k1 = list(map(lambda x : x >= 50, list1))
print(k1)  # [False, True, True, True, False]


# -----------------------------------------------------------

from functools import reduce

ans = reduce(lambda x,y : x+y, list1)   # [10, 90, 89, 56, 32]

print(ans)  # 277


from itertools import accumulate

res = list(accumulate( list1, lambda x,y : x+y))
print(res)   # [10, 100, 189, 245, 277]
# list1 = [[1,1,0], [0,1,1], [1,1,1], [1,2,2], [2,0,0]]

list1 = []

# import numpy

# import random

# numpy.random()


list1  = [1,1,1,0,2,1,1,2,32,3,2]

# 1 ---> [0,1,2,5,6]
# 0 ---> [3]


unique = []

for i in list1:
    if i not in unique:
        unique.append(i)

for i in unique:
    res=  []
    for j in range(len(list1)):
        if i == list1[j]:
            res.append(j)
    print(i,'----> ',res)
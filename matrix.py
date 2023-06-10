matrix = [[89,67,32], 
          [21,90,78], 
          [32,43,56]]


# 89 90 56
sum=0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            sum+=matrix[i][j]

print(sum)


# 
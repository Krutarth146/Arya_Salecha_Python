def check(list1, val):
    x = len(list1)//2
    first = list1[:x]  # list1[0:4]
    second = list1[x:]  # list1[4:]
    temp = []
    if val == True:
        for j,k in zip(first,second):
            temp.append(j)
            temp.append(k)

    else:
        for j,k in zip(first,second):
            temp.append(k)
            temp.append(j)
    return temp


print(check([5,6,7,8,1,2,3,4], False))


# -------------------------------------------------------


# Dictionary

# key - Values Pairs

dict1 = {}

print(type(dict1))   # Dict

set1 = {}
set1 = {10}
print(type(set1))  # set

dict2 = {'Name' : "Aaryan", 'roll' : 90, 'address' : ['Ahm', 'Gnr'], 'Name' : 'Amit'}

print(dict2)   # {'Name': 'Amit', 'roll': 90, 'address': ['Ahm', 'Gnr']}

# keys ---> Name, roll, address  (Unique)
# Values ---> Allow's Duplicates

set2 = set()
print(type(set2))   # <class 'set'>

# Ordered (No Index), Don't Allow Duplicates, Mutable (Changeble)
dict2 = {'Name' : "Aaryan", 'roll' : 90, 'address' : [{'city' : ['Ahm', 'Gnr']}, (10,20)], 'Name' : 'Amit'}

print(dict2['Name'])  # Amit
print(dict2['address'])  # [{'city': ['Ahm', 'Gnr']}]
print(dict2['address'][0]['city'])  # ['Ahm', 'Gnr']
print(dict2['address'][0]['city'][1][1:])  # nr

dict2.update({'Today' : 21, 'TOmorrow' : 22})
print(dict2)   # {'Name': 'Amit', 'roll': 90, 'address': [{'city': ['Ahm', 'Gnr']}, (10, 20)], 'Today': 21, 'TOmorrow': 22}

print(dict2.get('Name1'))  # None
# print(dict2['Name1'])   # Generates an Error if key is Not Found



for key,val in dict2.items():
    # print(val)   # ('TOmorrow', 22)

    if val == 90:
        print(key)   # roll
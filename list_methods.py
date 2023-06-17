# List Methods   # Mutable (Changeble)

list1 = [10,290,89,79,67,56]
print(len(list1))   # 6

list1.append(9000)
print(list1)   # [10, 290, 89, 79, 67, 56, 9000]


# lst2 =  [int(i) for i in input().split()]  # List Comprehension

# print(lst2)

# list1.extend(lst2)   # [10, 290, 89, 79, 67, 56, 9000, 10, 90, 89, 78]
# list1.append(lst2)   # [10, 290, 89, 79, 67, 56, 9000, [10, 90, 89, 78, 67]]

list1.extend('4000')
list1.append("Salecha")
print(list1)

 #                     [10, 290, 89, 79, 67, 56, 9000, '4', '0', '0', '0', 'Salecha']
list1.insert(2, 9050)# [10, 290, 9050, 89, 79, 67, 56, 9000, '4', '0', '0', '0', 'Salecha']
list1.insert(-1, 3050)# [10, 290, 9050, 89, 79, 67, 56, 9000, '4', '0', '0', '0', 'Salecha']
print(list1)  # [10, 290, 9050, 89, 79, 67, 56, 9000, '4', '0', '0', '0', 3050, 'Salecha']

list1[-1] = "Royal"
print(list1)  # [10, 290, 9050, 89, 79, 67, 56, 9000, '4', '0', '0', '0', 3050, 'Royal']

# Remove Elements

print(list1.pop())
print(list1)  # [10, 290, 9050, 89, 79, 67, 56, 9000, '4', '0', '0', '0', 3050]

list1.pop(2)
print(list1)   # [10, 290, 89, 79, 67, 56, 9000, '4', '0', '0', '0', 3050]

list1.remove(9000)
print(list1)  # [10, 290, 89, 79, 67, 56, '4', '0', '0', '0', 3050]

list2 = list1   # Deep Copy

list3 = list1.copy()  # Shallow Copy  # Xerox

# Arya Patel

list1.append(8000)
print(list2)  # [10, 290, 89, 79, 67, 56, '4', '0', '0', '0', 3050, 8000]
print(list3)  # [10, 290, 89, 79, 67, 56, '4', '0', '0', '0', 3050]

print(id(list1))  # 2117413251648
print(id(list2))  # 2117413251648
print(id(list3))  # 2117417486976



'''
Task-:
1. Create a list of Fruits(15 exotic fruits)
take user input and check if the fruits are avail in the list
if available print "fruit_name is Available"


2. create a list of numbers(15 numbers (1-100))
sort that list in ascending order
search for the number in the list
take input from user and find all the occurence
print the occurence


Tasks-: 
    1. Wap to find no. of month from the given no. of days
    2. wap to scan seconds and print hour, minute and remaining seconds
    3. wap to swap 3 numbers that is scanned by the user (a->b, b->c, c->a)
    4. wap to check whether the number is odd or even
    5. wap to find out the maximum, minimum, average of the numbers that is scanned by the user
    6. wap to make any user inputted string in uppercase or lowercase
    7. wap to print the sum of user entered numbers (scan by the user)
    8. wap to find power of a number
    9. wap to print numbers between n1 and n2 (n1, n2 are scanned by the user)
    
    Finale-: Make a Python program that generates a list of powers of base that is given by user upto the power given by user.    
    eg: base = 2, power=10
    output: [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    list programs
    1. add 5 numbers into the list and print the list
    2. add 10 numbers into the list, reverse that list, store the list into another list and print the list
    3. add 10 numbers into the list, sort that list and print the list
    4. add 10 numbers into the list, remove the duplicates and print the list
    5. add 10 numbers into the list, print the maximum and minimum number from the list
    6. add 10 numbers into the list, print the average of the list
    7. add 10 numbers into the list, print the sum of the list
    8. scan 5 numbers from the user and store it into the list, check if both the lists are same or not
    9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
    # Ask user for quantity
    # Assume each unit's cost is 100.
    # Judge and print total cost for user. 

    10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

    11. A school has following rules for grading system:
    # a. Below 25 - F
    # b. 25 to 45 - E
    # c. 45 to 50 - D
    # d. 50 to 60 - C
    # e. 60 to 80 - B
    # f. Above 80 - A
    # Ask user to enter marks and print the corresponding grade.

    12. A student will not be allowed to sit in exam if his/her attendance is less than 75%.
    # Take following input from user:
    # Number of classes held
    # Number of classes attended.
    # And print:
    # percentage of class attended
    # Is student is allowed to sit in exam or not.

'''

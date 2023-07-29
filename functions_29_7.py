# Functions


# void Arya();   // Func. Declaration

# Arya():    # Func. Defination
#     casesd
#     c
#     sdcvs
#     dc
#     sdc
#     sd
#     case


# Inbuilt Function
# print("Hello")
# input()


# Arya();  // Func. Calling

# Func. Defination
# Func. Calling


def Arya():
    print("Hello Arya Salecha")   # Func. Defination


Arya()
Arya()
# Func. 4 Types

# 1. Without Return type and Without Args
# 2. Without Return type and With Args
# 3. With Return type and Without Args
# 4. With Return type and With Args

# 1. Without Return type and Without Args

def Arya1():
    a,b = 10,20
    print(a+b)

Arya1()   # 30


# 2. Without Return type and With Args

def Patel(num1 = 43, num2 = "Aman"):   # Default Function
    print(num1,num2)

# Patel(23,"Manoj")   # 23 Manoj
Patel(32, True)   # 32 True

# --------------------------

x = 10   # Global Var
 
def Dhruv():
    x = 30   # Local Var
    x+=10
    print(x)  # 40

Dhruv() # 40
print(x*2)  # 80

x = 10

def Kru():
    global x
    x+=30
    print(x)   # 40
 
Kru()
print(x)  # 40


# ------------------------------------------


def Royal(num1, *kru, n4 = 56):
    print(kru)  # 266
    print(type(kru))   # <class 'tuple'>
    print(len(kru))   # 5

    print(kru[-1][-2])  # 20

    for i in kru:
        print(i)

Royal(10,2,3,"str1", [10,20,30])   # (10, 2, 3, 'str1', [10, 20, 30])


# list1 = [10,20,30]   # List is mutable (Changeble)
# t1 = tuple(list1)


# tup1 = ()   # tuple
# tup1 = (10)   # int
# tup1 = (10,)  # tuple

# print(type(tup1))   # Tuple Is Immutable  (Not Changeble)


list1 = [10,151, 42, 153, 8208]

ans = [0,0,0,1,1]
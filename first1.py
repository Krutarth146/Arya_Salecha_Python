# int x = 90;

# x = 90
# print(type(x))  # <class 'int'>


# # Single Line Comment

# '''
# Multi
# Line
# Comment
# '''

# print("Hello")


# print('Hello Arya Salecha',end='_')  # Default - \n
# print("Good Evening")


# x = "Good"
# dhiraj_sir = "Boy"

# print(x,dhiraj_sir,sep='__Center__')

# print('''
#     Arya Salecha
#     Address: 
#         Ahm
#         380001
#     ''')

# a = input()
# print(a)
# print(type(a))  # <class 'str'>

# a = int(input())
# print(type(a))  # <class 'int'>

# Typecasting   1. Implicit Typecasting   2. Explicit Typecasting

x = 90
print(type(x))  # int

y = 89.90
print(type(y))  # float

g = 'A'
print(type(g))   # <class 'str'>

h = True
print(type(h))

d = 56 + 90j
print(type(d))  # <class 'complex'>  56 is real part, 90j is Imaginary Part

h = 90
print(d+h)  # (146+90j)  # Implicit Typecasting


f = True  # convert into 1
k = 90
print(f+k)   # 91  # Implicit Typecasting

x = "400.90"
print(int(float(x)))  # 400  # Explicit Typecasting

print(18/4)  # 4.5
print(-18//4)  # -5


num1 = int(input("ENter first NUmber: "))
num2 = int(input("ENter second NUmber: "))
print("sum:",num1,"+",num2,'=',num1 + num2)   # 25
print(f"sub: {num1} + {num2} = {num1-num2}")
print(f"Mul: {num1} * {num2} = {num1*num2}")
print(f"Div: {num1} / {num2} = {num1/num2}")
print(f"floor div: {num1} // {num2} = {num1//num2}")
print(f"Modulas: {num1} % {num2} = {num1%num2}")
print(f"Exp: {num1} ** {num2} = {num1**num2}")
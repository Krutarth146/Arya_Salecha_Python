def Arya(n1,n2,*kru,n5=90):
    print(kru)
    print(type(kru))   # <class 'tuple'>

    print(kru[-2])   # 30

Arya(10,20,30,[10,20])   # (10, 20, 30, [10, 20])


def Salecha(*args, **kwargs):

    print(kwargs)  # {'name': 'Arya', 'surname': 'Salecha'}
    print(kwargs['name'])   # Arya

Salecha(10,20,30,40,name="Arya", surname= 'Salecha')


# ----------------------------------------

# lambda

def square(num):
    return num ** 2

print(square(5))

# lambda (Anounoumous Function)   One Liner

arya = lambda num : num ** 2
print(arya(40))   # 1600


t1 = lambda num, n1 = 10 : num ** 3 + n1
print(t1(3))   # 37


# (a*x**2) + (b*x) + (c)

# a,b,c

def quadratic_fun(a1, b1, c1):
    return lambda x :  (a1*x**2) + (b1*x) + (c1)

royal = quadratic_fun(1,5,6)
print(royal(10))  # 156


str1 = "arYa Salecha"


max = lambda x,y,z : (x if x > z else z) if x > y else (y if y>z else z)
print(max(30,90,2100))
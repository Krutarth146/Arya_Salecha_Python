# Type - 3  without ARgs and With Return Type

def Arya():
    a=1+2

    print(a)   # 3
    return a

print(Arya())  # 3


balance= 90000
def deposit(amount):
    global balance

    balance += amount
    return balance

x = deposit(50000)

def check_balance(x):
    print(x)


check_balance(x)

# -----------------------------

def patel():
    return "Manoj", 90, 899.78


x = patel()
print(x[0][:-2])  

# --------------------------


# Type - 4 

# 4. With Return type and With Args

def royal(num1, num2):
    return num1 + num2 - 5

print(royal(10,90))   # 95




def series(num):
    for i in range(1,num+1):
        return i   # Iterator

print(series(5))


def series(num):
    for i in range(1,num+1):
        yield i   # Generator


# print(series(5))   # <generator object series at 0x000001C4F2459A10>

# print(series(5).__next__())

x = series(5)
print(x.__next__())  # 1
print(x.__next__())  # 2

for i in series(5):
    print(i)
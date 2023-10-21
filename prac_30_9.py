# def Aman():
#     def Manoj():
#         print('Manoj is Good Boy')
#     print('Aman is Good Boy.')
#     return Manoj()

# Aman()


def Ashok(Rishita):

    print('-----')
    return Rishita()

@Ashok    # Decorator
def Arya():
        print('Arya is Naughty Boy.')

# Ashok(Arya)


def Kru(list1):
      list1.append(45200)
      print(list1)

aman = [10,20,30,40,]
Kru(aman)

aman.append(3400)
print(aman)   # [10,20,30,40,45200,3400]



def Kru(x1):
      x1 += 100  
      print(x1)   # 150

aman = 50
Kru(aman)

aman += 34
print(aman)   # 84



list1 = [10,202,3022,4,503]

ans = [2,3,4,1,3]
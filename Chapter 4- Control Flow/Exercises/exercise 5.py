##Exercise No.5
Favourite_Fruits=[]
n = int(input("Number of fuits you love : "))
for i in range(0,n):
  List = str(input())
  Favourite_Fruits.append(List)
print(Favourite_Fruits)  
if 'apple' in Favourite_Fruits:
  print("you really like Apples")
if 'banana' in Favourite_Fruits:
  print("you really like Bananas")
if 'watermelon' in Favourite_Fruits:
  print("you really like WaterMelon")
if 'orange' in Favourite_Fruits:
  print("you really like Oranges")
if 'mango' in Favourite_Fruits:
  print("you really like Mangos")

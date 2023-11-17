#extra 5
#ticket price
total = 0
x = 0
while x<5:
    age = int(input("Enter age : "))
    if age>3:
        total += 100
    else:
      print("you are free")
    x +=1
print(total)
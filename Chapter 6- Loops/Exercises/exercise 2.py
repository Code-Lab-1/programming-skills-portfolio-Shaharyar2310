#exercise 2
print("Enter 0 to stop entring age")
while True:
  age = int(input("Enter you age here : "))
  if age == 0:
    break
  elif age<3:
    print('free')
  elif age>=3 and age<=12:
    print('$10')
  elif age>12:
    print('$15')

##exercise No. 4
age = int(input("Enter persons age here : "))
print("persons age is",age,"yeras")
if age<=1:
  print("person is a baby")
elif age>=2 and age<=4:
  print("person is a toddler")
elif age>=4 and age<=13:
  print("person is a kid")
elif age>=13 and age<=20:
  print("person is a teenager")
elif age>=20 and age<=65:
  print("person is an adult")
elif age>=65:
  print("person ia an elder")
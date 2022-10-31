#exercise 1
toppings=[]
print("To stop adding toppings enter quit,")
while True:
  topping=input("Enter the topping : ")
  if topping == 'quit':
    break
  else:
    print("I will add",topping, "to your pizza ",)
    toppings.append(topping)
   
print("you toppings are : ",toppings)
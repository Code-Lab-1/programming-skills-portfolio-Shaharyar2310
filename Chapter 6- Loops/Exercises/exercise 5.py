#exercise 5 
finihed_sandwich_orders=[]
sandwich_orders=["Chicken Sandwich.","pastrami sandwich.","Egg Sandwich.","Seafood Sandwich.",
"Roast Beef Sandwich.","pastrami sandwich.","Grilled Cheese.","pastrami sandwich.","Nutella Sandwich.","pastrami sandwich.",
"Grilled Chicken Sandwich.","pastrami sandwich.","pastrami sandwich."]
print(sandwich_orders)
print("we are out of ingrediants for pistrami sandwich")
while 'pastrami sandwich.' in sandwich_orders:
  sandwich_orders.remove('pastrami sandwich.')
while True:
  if sandwich_orders == []:
    break
  else:
    print("I made your", sandwich_orders[0])
    finihed_sandwich_orders.insert(0,sandwich_orders[0])
    sandwich_orders.pop(0)

print("left orders : ",sandwich_orders)
print("finished orders : ",finihed_sandwich_orders)